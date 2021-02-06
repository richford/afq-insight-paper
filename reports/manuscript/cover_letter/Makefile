LATEX=xelatex
LATEXOPT=--shell-escape
NONSTOP=--interaction=nonstopmode

LATEXMK=latexmk
LATEXMKOPT=-pdf
CONTINUOUS=-pvc

MAIN=cover_letter

SOURCES=$(MAIN).tex Makefile

all: coverletter

.refresh:
	touch .refresh

coverletter: $(MAIN).tex .refresh Makefile
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) \
		-pdflatex="$(LATEX) $(LATEXOPT) $(NONSTOP) %O %S" $(MAIN)

force:
	touch .refresh
	rm -f $(MAIN).pdf
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) \
		-pdflatex="$(LATEX) $(LATEXOPT) %O %S" $(MAIN)

clean:
	$(LATEXMK) -C
	rm -f $(MAIN).pdfsync
	rm -rf *~ *.tmp
	rm -f *.bbl *.blg *.aux *.end *.fls *.log *.out *.fdb_latexmk

once:
	$(LATEXMK) $(LATEXMKOPT) -pdflatex="$(LATEX) $(LATEXOPT) %O %S"

debug:
	$(LATEX) $(LATEXOPT) $(MAIN)
	$(LATEX) $(LATEXOPT) $(MAIN)

spell: $(addsuffix .spchk,$(basename $(SOURCES)))

%.spchk: %.tex
	@aspell --lang=en --home-dir=. --personal=dictionary.txt -t -c $<

.PHONY: clean force once all spell docx coverletter
