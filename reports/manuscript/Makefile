LATEX=pdflatex
BIBTEX=bibtex
REPORT=paper

SRCS=$(wildcard *.tex)
REFS=$(wildcard *.bib)
FIGS=$(wildcard figures/*)

all: $(SRCS) $(REFS) $(FIGS)
	$(LATEX) $(REPORT)
	$(BIBTEX) $(REPORT)
	$(LATEX) $(REPORT)
	$(LATEX) $(REPORT)

clean:
	rm -f *~ *.dvi *.aux *.out *.log *.blg *.bbl $(REPORT).ps $(REPORT).pdf sections/*.aux comment.cut
