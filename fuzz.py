import traceback
from typing import Any, List
from detect_test import checkTestFile
from generation.attack_model import calculate_k, perform_inference
from generation.loss_based_label_perturbation import label_flip_perturbation
from generation.probability_based_label_perturbation import generate_malicious_instance

def fuzz(method, fuzzed_arguments: List[Any]):
    for arguments in fuzzed_arguments:
        try:
            result = method(*arguments)
        except Exception as exc:
            print(f"Fuzz: {method.__name__} FAIL")
            traceback.print_exc()
        else:
            print(f"Fuzz: {method.__name__} PASS ({result})")

if __name__ == "__main__":
    fuzz_targets = [
        (
            checkTestFile, [
                (None),
                ('falsestring'),
                (1.0),
                ('/')
            ]
        ),
        (
            calculate_k, [
                (None, None, None, None),
                ('false', 'string', 'no', 'use'),
                (1.0, 2.0, 3.0, 4.0),
                (',', '?', '.', '!')
            ]
        ),
        (
            perform_inference, [
                (None, None, None, None, None),
                ('false', 'string', 'no', 'good', 'use'),
                (1.0, 2.0, 3.0, 4.0, 5.0),
                (';', ':', '&', '*', '(')
            ]
        ),
        (
            label_flip_perturbation, [
                (None, None, None, None, None, None, None),
                ('no', 'good', 'use', 'false', 'string', 'fake', 'here'),
                (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0),
                ('[', ']', '{', '}', '#', '@', '$')
            ]
        ),
        (
            generate_malicious_instance, [
                (None, None, None),
                ('bad', 'string', 'use'),
                (1.0, 2.0, 3.0),
                ('=', '+', '-')
            ]
        )
    ]
    for method, fuzzed_arguments in fuzz_targets:
        fuzz(method, fuzzed_arguments)