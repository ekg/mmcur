# Makefile for building LaTeX document

# Main document name without extension
TARGET = main

# LaTeX compiler and options
LATEX = xelatex
LATEX_OPTS = -interaction=nonstopmode -halt-on-error

# Default target
all: $(TARGET).pdf

# Build PDF
$(TARGET).pdf: $(TARGET).tex
	$(LATEX) $(LATEX_OPTS) $(TARGET)
	$(LATEX) $(LATEX_OPTS) $(TARGET)  # Second run for references

# Clean auxiliary files
clean:
	rm -f $(TARGET).aux $(TARGET).log $(TARGET).out $(TARGET).toc \
		$(TARGET).bbl $(TARGET).blg $(TARGET).synctex.gz

# Clean everything including PDF
distclean: clean
	rm -f $(TARGET).pdf

.PHONY: all clean distclean
