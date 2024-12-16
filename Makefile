# Makefile for building LaTeX document

# Main document name without extension
TARGET = main

# LaTeX compiler and options
LATEX = pdflatex
LATEX_OPTS = -interaction=nonstopmode -halt-on-error

# Default target
all: $(TARGET).pdf

# Build PDF
$(TARGET).pdf: $(TARGET).tex refs.bib
	$(LATEX) $(LATEX_OPTS) $(TARGET)
	bibtex $(TARGET)
	$(LATEX) $(LATEX_OPTS) $(TARGET)
	$(LATEX) $(LATEX_OPTS) $(TARGET)  # Final run for references

# Clean auxiliary files
clean:
	rm -f $(TARGET).aux $(TARGET).log $(TARGET).out $(TARGET).toc \
		$(TARGET).bbl $(TARGET).blg $(TARGET).synctex.gz

# Clean everything including PDF
distclean: clean
	rm -f $(TARGET).pdf

.PHONY: all clean distclean
