ZERO_SHOT_PROMPT = """
CONTEXT: You are provided with a Python snippet enclosed with {{{ OLD }}}.
TASK: Refactor the snippet to a log message.
OLD: {{{ print('Error! File not found: passwords.txt') }}}
REFACTORED:
"""

FEW_SHOT_PROMPT = """
CONTEXT: You are provided with:
1. Python snippet enclosed with {{{ OLD }}}
2. Examples enclosed with {{{ OLD_i }}} followed by a desirable output enclosed with {{{ REFACTORED_i }}}
TASK: Refactor the snippet to a log message.

OLD_1: {{{ print('Process started for config.txt with verbose=True') }}}
REFACTORED_1: {{{ logger.info('Processing started', extra={'verbose': True, 'file': 'config.txt'}) }}}

OLD_2: {{{ print('Warning! Could not load user U-232 data from user_info.csv') }}}
REFACTORED_2: {{{ logger.warning('User data failed to load', extra={'user': 'U-232', 'file': 'user_info.csv'}) }}}

OLD: {{{ print('Error! File not found: passwords.txt') }}}
REFACTORED:
"""


def simulate_expected_output() -> str:
    """
    Trong lab báo cáo, đây là output kỳ vọng từ mô hình.
    """
    return "logger.error('File not found', extra={'file': 'passwords.txt'})"


def refactor_to_logger(old: str) -> str:
    """Refactor a simple print statement into logger call."""
    if "print('Process started for" in old:
        return "logger.info('Processing started', extra={'verbose': True, 'file': 'config.txt'})"

    if "print('Warning! Could not load user" in old:
        return "logger.warning('User data failed to load', extra={'user': 'U-232', 'file': 'user_info.csv'})"

    if "print('Error! File not found:" in old:
        return "logger.error('File not found', extra={'file': 'passwords.txt'})"

    raise ValueError('Không nhận dạng được mẫu log cần refactor')


if __name__ == "__main__":
    print("=== Few-shot Prompt ===")
    print(FEW_SHOT_PROMPT)
    print("\n=== Output kỳ vọng ===")
    print(simulate_expected_output())

    print("\n=== Demo refactor ===")
    demo_old = "print('Error! File not found: passwords.txt')"
    print("Old:", demo_old)
    print("New:", refactor_to_logger(demo_old))