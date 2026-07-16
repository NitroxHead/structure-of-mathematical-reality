# The Structure of Mathematical Reality: build pipeline
#
#   curriculum.md            the BLUEPRINT: scope, readings, schedule,
#                            and the seed content for chapter documents.
#   chapters/chNN-*/[doc].md the COURSE: seeded from the blueprint, then
#                            expanded by hand. Files carrying an
#                            '<!-- AUTHORED -->' marker are first-class
#                            content and are never reseeded.
#   build/chNN-*/[doc].{tex,pdf}
#                            generated print layer. Never hand-edited,
#                            never committed. Delete it freely.
#
#   make            render + compile everything from chapter markdown
#   make render     markdown -> tex only
#   make book       stitch the 17 lectures into a single build/book.pdf
#   make reseed     re-derive chapter markdown from curriculum.md
#                   (skips files with an AUTHORED marker)
#   make clean      remove LaTeX aux files
#   make distclean  remove the entire build/ tree (markdown stays)

SHELL := /bin/bash
STYDIR := $(CURDIR)/shared
BUILD  := $(CURDIR)/build

.PHONY: all render reseed pdf book clean distclean

all: pdf
	@echo "Build complete."

reseed:
	@echo "Reseeding chapter markdown from curriculum.md (AUTHORED files preserved)..."
	@python3 scripts/split_curriculum.py | grep -E "preserved|WARNING|Summary" || true
	@echo "Reseed done."

render:
	@python3 scripts/render_tex.py
	@echo "Rendered: markdown -> tex."

# After render has run, build every tex found under build/.
pdf: render
	@set -e; for f in "$(BUILD)"/ch*/[a-z]*.tex; do \
		d=$$(dirname "$$f"); b=$$(basename "$$f"); \
		echo "  pdflatex $${f#$(CURDIR)/}"; \
		(cd "$$d" && TEXINPUTS="$(STYDIR):$$TEXINPUTS" \
			pdflatex -interaction=nonstopmode -halt-on-error "$$b" > /dev/null && \
			TEXINPUTS="$(STYDIR):$$TEXINPUTS" \
			pdflatex -interaction=nonstopmode -halt-on-error "$$b" > /dev/null) || \
			{ echo "FAILED: $$f (see $$d/$${b%.tex}.log)"; exit 1; }; \
	done
	@$(MAKE) --no-print-directory clean
	@echo "PDFs built."

# Assemble the lectures into one book and compile it (two passes for the TOC).
book:
	@python3 scripts/render_book.py
	@echo "  pdflatex build/book.tex"
	@set -e; cd "$(BUILD)" && TEXINPUTS="$(STYDIR):$$TEXINPUTS" \
		pdflatex -interaction=nonstopmode -halt-on-error book.tex > /dev/null && \
		TEXINPUTS="$(STYDIR):$$TEXINPUTS" \
		pdflatex -interaction=nonstopmode -halt-on-error book.tex > /dev/null || \
		{ echo "FAILED: book.tex (see build/book.log)"; exit 1; }
	@$(MAKE) --no-print-directory clean
	@echo "build/book.pdf built."

clean:
	@rm -f "$(BUILD)"/ch*/*.aux "$(BUILD)"/ch*/*.log "$(BUILD)"/ch*/*.out \
	       "$(BUILD)"/ch*/*.toc "$(BUILD)"/ch*/*.nav "$(BUILD)"/ch*/*.snm "$(BUILD)"/ch*/*.vrb
	@rm -f "$(BUILD)"/book.aux "$(BUILD)"/book.log "$(BUILD)"/book.out "$(BUILD)"/book.toc
	@echo "Cleaned aux files."

distclean:
	@rm -rf "$(BUILD)"
	@echo "Removed build/."
