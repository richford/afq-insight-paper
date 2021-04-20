import AFQ.data as afqd
import afqinsight as afqi
import json
import nibabel as nib
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from AFQ.viz.plotly_backend import visualize_volume
from plotly.subplots import make_subplots


def plot_coefs_on_bundle_cores(
    results,
    key,
    columns,
    metric="fa",
    use_pyafq_bundle_names=False,
    linewidth=15,
    coef_func=(
        None,
        "abs_mean",
    ),
    eye=None,
    center=None,
    width=500,
    height=500,
):
    my_results = results[key][0]
    if all(["pca_components" in bag_res for bag_res in my_results.values()]):
        mean_beta = np.mean([
            np.einsum(
                "...j,...jk",
                np.mean(my_results[cv_idx]["coefs"], axis=0).reshape(
                    np.array(my_results[cv_idx]["pca_components"]).shape[:2]
                ),
                np.array(my_results[cv_idx]["pca_components"]),
            ).flatten() for cv_idx in my_results.keys()
        ], axis=0)
    else:
        mean_beta = np.mean(np.array(
            [np.array(bag_res["coefs"]) for bag_res in my_results.values()]
        ), axis=(0, 1))
    with open("../data/raw/core_streamlines.json") as fp:
        cores = json.load(fp)

    index = pd.MultiIndex.from_tuples(columns, names=["metric", "tractID", "nodeID"])
    beta_hats = afqi.beta_hat_by_groups(mean_beta, columns=index, drop_zeros=True)

    bad_keys = [k for k in beta_hats.keys() if "Cingulum Hippocampus" in k]
    for key in bad_keys:
        _ = beta_hats.pop(key, None)

    new_cores = {}
    if use_pyafq_bundle_names:
        for key, val in cores.items():
            if (
                key in afqd.BUNDLE_MAT_2_PYTHON
                and afqd.BUNDLE_MAT_2_PYTHON[key] in beta_hats
            ):
                new_cores[afqd.BUNDLE_MAT_2_PYTHON[key]] = val
    else:
        for key, val in cores.items():
            if key in beta_hats:
                new_cores[key] = val

    cores = new_cores

    bundle_names = beta_hats.keys()
    bundles = {bn: np.array(cores[bn]["coreFiber"]) for bn in cores.keys()}

    def color_transform(betas, func):
        if func is None:
            return betas
        if func == "abs_max":
            return np.max(np.abs(betas)) * np.ones_like(betas)
        if func == "abs_mean":
            return np.mean(np.abs(betas)) * np.ones_like(betas)
        if func == "abs":
            return np.abs(betas)

    colors = {
        row: {bn: color_transform(beta_hats[bn][metric], func) for bn in cores.keys()}
        for row, func in enumerate(coef_func)
    }

    max_color = {
        row: np.max(np.abs(np.concatenate(list(_color.values()))))
        if coef_func[row] != "abs"
        else np.max(np.concatenate(list(_color.values())))
        for row, _color in colors.items()
    }

    min_color = {
        row: 0.0
        if coef_func[row] == "abs"
        else -max_color[row]
        if coef_func[row] is None
        else 0.0
        for row, _color in colors.items()
    }

    color_maps = {
        row: "oxy" if coef_func[row] is None else "dense" for row in max_color.keys()
    }

    locs = (np.arange(len(coef_func)) * 2 + 1)[::-1]
    cbar_locs = {row: locs[row] / (2.0 * len(coef_func)) for row in max_color.keys()}
    cbar_len = 0.97 / len(coef_func)

    fig = make_subplots(
        rows=len(coef_func),
        specs=[[{"type": "surface"}]] * len(coef_func),
        vertical_spacing=0.0,
        horizontal_spacing=0.0,
    )

    volume = nib.load(
        "../data/external/tpl-MNI152NLin2009cAsym_res-01_T2w.nii.gz"
    ).get_fdata()

    offset = tuple(v // 2 for v in volume.shape)
    for ckey, color in colors.items():
        for bn, _bundle in bundles.items():
            fig.add_trace(
                go.Scatter3d(
                    x=_bundle[:, 0] + offset[0],
                    y=_bundle[:, 1] + offset[1] + 20,
                    z=_bundle[:, 2] + offset[2] - 4,
                    mode="lines",
                    line={
                        "color": color[bn],
                        "width": linewidth,
                        "colorscale": color_maps[ckey],
                        "cmin": min_color[ckey],
                        "cmax": max_color[ckey],
                        "showscale": True,
                        "colorbar": dict(
                            len=cbar_len,
                            y=cbar_locs[ckey],
                            tickfont=dict(size=22),
                        ),
                    },
                    hovertext=bn,
                    showlegend=False,
                    name=bn,
                ),
                row=ckey + 1,
                col=1,
            )

        fig.update_layout(
            scene=dict(
                annotations=[
                    dict(
                        text="ARCR",
                        x=bundles.get("ARC_R", bundles.get("Right Arcuate"))[
                            10, 0
                        ]
                        + offset[0],
                        y=bundles.get("ARC_R", bundles.get("Right Arcuate"))[
                            10, 1
                        ]
                        + offset[1]
                        + 20,
                        z=bundles.get("ARC_R", bundles.get("Right Arcuate"))[
                            10, 2
                        ]
                        + offset[2]
                        - 4,
                        showarrow=True,
                        xanchor="center",
                        font=dict(size=20),
                        yanchor="middle",
                        ax=10,
                        ay=-50,
                        arrowsize=2,
                        arrowwidth=1,
                        arrowhead=1,
                    ),
                    dict(
                        text="ARCL",
                        x=bundles.get("ARC_L", bundles.get("Left Arcuate"))[
                            10, 0
                        ]
                        + offset[0],
                        y=bundles.get("ARC_L", bundles.get("Left Arcuate"))[
                            10, 1
                        ]
                        + offset[1]
                        + 20,
                        z=bundles.get("ARC_L", bundles.get("Left Arcuate"))[
                            10, 2
                        ]
                        + offset[2]
                        - 4,
                        showarrow=True,
                        xanchor="center",
                        font=dict(size=20),
                        yanchor="middle",
                        ax=10,
                        ay=-70,
                        arrowsize=2,
                        arrowwidth=1,
                        arrowhead=1,
                    ),
                    dict(
                        text="CSTR",
                        x=bundles.get("CST_R", bundles.get("Right Corticospinal"))[
                            -1, 0
                        ]
                        + offset[0],
                        y=bundles.get("CST_R", bundles.get("Right Corticospinal"))[
                            -1, 1
                        ]
                        + offset[1]
                        + 20,
                        z=bundles.get("CST_R", bundles.get("Right Corticospinal"))[
                            -1, 2
                        ]
                        + offset[2]
                        - 4,
                        showarrow=True,
                        xanchor="center",
                        font=dict(size=20),
                        yanchor="middle",
                        ax=-50,
                        ay=10,
                        arrowsize=2,
                        arrowwidth=1,
                        arrowhead=1,
                    ),
                    dict(
                        text="CSTL",
                        x=bundles.get("CST_L", bundles.get("Left Corticospinal"))[-1, 0]
                        + offset[0],
                        y=bundles.get("CST_L", bundles.get("Left Corticospinal"))[-1, 1]
                        + offset[1]
                        + 20,
                        z=bundles.get("CST_L", bundles.get("Left Corticospinal"))[-1, 2]
                        + offset[2]
                        - 4,
                        showarrow=True,
                        xanchor="center",
                        font=dict(size=20),
                        yanchor="middle",
                        ax=50,
                        ay=10,
                        arrowsize=2,
                        arrowwidth=1,
                        arrowhead=1,
                    ),
                    dict(
                        text="CFA",
                        x=bundles.get("FA", bundles.get("Callosum Forceps Minor"))[
                            85, 0
                        ]
                        + offset[0],
                        y=bundles.get("FA", bundles.get("Callosum Forceps Minor"))[
                            85, 1
                        ]
                        + offset[1]
                        + 20,
                        z=bundles.get("FA", bundles.get("Callosum Forceps Minor"))[
                            85, 2
                        ]
                        + offset[2]
                        - 4,
                        showarrow=True,
                        xanchor="center",
                        font=dict(size=20),
                        yanchor="middle",
                        ax=10,
                        ay=40,
                        arrowsize=2,
                        arrowwidth=1,
                        arrowhead=1,
                    ),
                ]
            ),
        )

    camera = dict(
        eye=dict(x=0.8, y=0.8, z=0.8) if eye is None else eye,
        center=dict(x=0, y=0, z=0) if center is None else center,
    )

    fig.update_layout(
        scene=dict(
            camera=camera,
            xaxis=dict(
                showbackground=False, showgrid=False, zeroline=False, visible=False
            ),
            yaxis=dict(
                showbackground=False, showgrid=False, zeroline=False, visible=False
            ),
            zaxis=dict(
                showbackground=False, showgrid=False, zeroline=False, visible=False
            ),
        ),
        scene2=dict(
            camera=camera,
            xaxis=dict(
                showbackground=False, showgrid=False, zeroline=False, visible=False
            ),
            yaxis=dict(
                showbackground=False, showgrid=False, zeroline=False, visible=False
            ),
            zaxis=dict(
                showbackground=False, showgrid=False, zeroline=False, visible=False
            ),
        ),
        autosize=False,
        width=width,
        height=height,
        margin=dict(l=0, r=0, t=0, b=0),
    )

    for row, loc in cbar_locs.items():
        if coef_func[row] is None:
            text = r"$\hat{\beta}$"
        elif coef_func[row] == "abs":
            text = r"$\left| \hat{\beta} \right|$"
        else:
            text = r"$\left\langle \left| \hat{\beta} \right| \right\rangle$"
        fig.add_annotation(
            text=text,
            xref="paper",
            yref="paper",
            x=1.03,
            y=loc + 0.12,
            showarrow=False,
            font=dict(size=48),
            yanchor="middle",
        )

    fig = visualize_volume(
        volume, figure=fig, show_x=False, show_y=False, show_z=True, opacity=0.1
    )

    return beta_hats, fig