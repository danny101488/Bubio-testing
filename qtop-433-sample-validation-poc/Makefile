SAMPLE_OUTPUT_DIR ?= build/sample-validation

.PHONY: sample-validation clean

sample-validation:
	python3 scripts/validate_sample_gate.py --output "$(SAMPLE_OUTPUT_DIR)"

clean:
	rm -rf build
