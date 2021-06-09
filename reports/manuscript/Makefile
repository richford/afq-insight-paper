LATEX=pdflatex
LATEXOPT=--shell-escape
NONSTOP=--interaction=nonstopmode

LATEXMK=latexmk
LATEXMKOPT=-pdf
CONTINUOUS=-pvc

MAIN=paper_changes
NOMARKUP=paper
SUPPLEMENT=supplemental_changes
SUPPLEMENTNOMARKUP=supplemental

SOURCES=$(MAIN).tex $(SUPPLEMENT).tex Makefile
FIGURES := $(shell find ../paper_figures/* -type f)

all: latex

.refresh:
	touch .refresh

latex: $(MAIN).tex $(NOMARKUP).tex Makefile $(FIGURES)
	$(LATEXMK) $(LATEXMKOPT) -pdflatex="$(LATEX) $(LATEXOPT)" $(MAIN).tex $(NOMARKUP).tex

# diff: $(MAIN).tex $(SUPPLEMENT).tex Makefile $(FIGURES)
# 	gsed -r 's/(\\mbox\{\\cite\{)([^\}]*)(\}\})/\\cite{\2}/g' $(MAIN).tex > $(MAIN)_no_mbox.tex
# 	python pyMergeChanges.py -ah $(MAIN)_no_mbox.tex $(NOMARKUP).tex
# 	rm $(MAIN)_no_mbox.tex
# 	python pyMergeChanges.py -ah $(SUPPLEMENT).tex $(SUPPLEMENTNOMARKUP).tex
# 	$(LATEXMK) $(LATEXMKOPT) -pdflatex="$(LATEX) $(LATEXOPT)" \
# 		$(MAIN).tex $(NOMARKUP).tex $(SUPPLEMENT).tex $(SUPPLEMENTNOMARKUP).tex

plos: $(MAIN).tex $(SUPPLEMENT).tex .refresh Makefile $(FIGURES)
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) \
		-pdflatex="$(LATEX) $(LATEXOPT) $(NONSTOP) %O %S" $(MAIN)

paper: $(MAIN).tex $(SUPPLEMENT).tex Makefile $(FIGURES)
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) $(MAIN).tex
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) $(SUPPLEMENT).tex

force:
	touch .refresh
	rm $(MAIN).pdf
	rm $(SUPPLEMENT).pdf
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) \
		-pdflatex="$(LATEX) $(LATEXOPT) %O %S" $(MAIN)
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) \
		-pdflatex="$(LATEX) $(LATEXOPT) %O %S" $(MAIN)
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) \
		-pdflatex="$(LATEX) $(LATEXOPT) %O %S" $(MAIN)

clean:
	$(LATEXMK) -C $(MAIN)
	rm -f $(MAIN).pdfsync
	rm -f $(SUPPLEMENT).pdfsync
	rm -rf *~ *.tmp
	rm -f *.bbl *.blg *.aux *.end *.fls *.log *.out *.fdb_latexmk
	rm -f sections/*.bbl sections/*.blg sections/*.aux sections/*.end sections/*.fls sections/*.log sections/*.out sections/*.fdb_latexmk

once:
	$(LATEXMK) $(LATEXMKOPT) -pdflatex="$(LATEX) $(LATEXOPT) %O %S" $(MAIN)

debug:
	$(LATEX) $(LATEXOPT) $(MAIN)
	$(LATEX) $(LATEXOPT) $(SUPPLEMENT)
	$(LATEX) $(LATEXOPT) $(MAIN)
	$(LATEX) $(LATEXOPT) $(SUPPLEMENT)

spell: $(addsuffix .spchk,$(basename $(SOURCES)))

%.spchk: %.tex
	@aspell --lang=en --home-dir=. --personal=dictionary.txt -t -c $<

docx:
	pandoc -s --biblio $(MAIN).bib $(MAIN).tex -o paper.docx

.PHONY: clean force once all spell docx paper
