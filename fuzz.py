import traceback
from typing import Any, List

from detection.main import chackAttackTest
from generation.main import generateUnitTest, generateAttack
from label_perturbation_attack.main import run_random_perturbation_experiment, call_prob

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
            chackAttackTest, [
                (None, None),
                ("wro", "rig"),
                (0, 1),
                ({}, {}),
                (5.0, 6.0),
                ('L7812', None)
            ]
        ),
        (
            generateUnitTest, [
                (None, None),
                ('lam', 'hci'),
                (87, 65),
                ([], {}),
                (0.0, 0.0),
                (None, 'ht.lm')
            ]
        )
        (
            generateAttack, [
                (None, None),
                ('lef', 'rig'),
                (2, 3),
                ([], []),
                (0.9, 0.8),
                ('/', None)
            ]
        ),
        (
            run_random_perturbation_experiment, [
                (None, None),
                ('aub', 'ari'),
                (9, 8),
                ({}, []),
                (2.3, 4.5),
                ('?', None)
            ]
        ),
        (
            call_prob, [
                (None, None, None),
                ('bie', 'pie', 'rit'),
                (5, 6, 7),
                ("", ".", ","),
                ([], [], []),
                (';', None)
            ]
        )
    ]
    for method, fuzzed_arguments in fuzz_targets:
        fuzz(method, fuzzed_arguments)