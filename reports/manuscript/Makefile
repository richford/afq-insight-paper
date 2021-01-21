LATEX=pdflatex
LATEXOPT=--shell-escape
NONSTOP=--interaction=nonstopmode

LATEXMK=latexmk
LATEXMKOPT=-pdf
CONTINUOUS=-pvc

MAIN=paper
SUPPLEMENT=supplemental

SOURCES=$(MAIN).tex $(SUPPLEMENT).tex Makefile $(shell find sections/* -type f)
FIGURES := $(shell find ../figures/* -type f)

all: nmeth

.refresh:
	touch .refresh

nmeth: $(MAIN).tex $(SUPPLEMENT).tex .refresh Makefile $(FIGURES)
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) \
		-pdflatex="$(LATEX) $(LATEXOPT) $(NONSTOP) %O %S" $(MAIN)

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

.PHONY: clean force once all spell docx
