import os
import subprocess
import time
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TESTS = [
    # Foundations
    ('foundations/tcp_echo', ['Hello Networks'], 'Echo: Hello Networks'),
    ('foundations/udp_echo', ['Ping UDP'], 'Echo: Ping UDP'),
    ('foundations/tcp_calculator', ['12', '+', '8'], 'Result: 20.0'),

    # Standard TCP
    ('standard_programs/tcp_01_factorial', ['5'], 'Factorial: 120'),
    ('standard_programs/tcp_02_even_odd', ['42'], 'The number is: Even'),
    ('standard_programs/tcp_03_square', ['7'], 'Square: 49'),
    ('standard_programs/tcp_04_string_length', ['network'], 'Length: 7'),
    ('standard_programs/tcp_05_string_reverse', ['socket'], 'Reversed: tekcos'),
    ('standard_programs/tcp_06_palindrome', ['radar'], 'Result: Palindrome'),
    ('standard_programs/tcp_07_uppercase', ['ethernet'], 'Uppercase: ETHERNET'),
    ('standard_programs/tcp_08_sum_of_digits', ['12345'], 'Sum of digits: 15'),
    ('standard_programs/tcp_17_word_count', ['Autonomous Systems and BGP Routing'], 'Word count: 5'),
    ('standard_programs/tcp_18_vowel_count', ['Computer Networks Laboratory'], 'Vowel count: 9'),

    # Standard UDP
    ('standard_programs/udp_09_string_length', ['packet'], 'Length: 6'),
    ('standard_programs/udp_10_even_odd', ['99'], 'The number is: Odd'),
    ('standard_programs/udp_11_string_reverse', ['protocol'], 'Reversed: locotorp'),
    ('standard_programs/udp_12_palindrome', ['level'], 'Result: Palindrome'),
    ('standard_programs/udp_13_square', ['9'], 'Square: 81'),
    ('standard_programs/udp_14_vowel_count', ['Transmission Control'], 'Vowel count: 6'),
    ('standard_programs/udp_15_uppercase', ['datagram'], 'Uppercase: DATAGRAM'),
    ('standard_programs/udp_16_replace_spaces_hyphens', ['hello world network test'], 'Modified message: hello-world-network-test'),
    ('standard_programs/udp_19_digit_count', ['Port 80 and 443'], 'Number of digits: 5'),

    # Core Experiments
    ('core_experiments/01_matrix_classification_tcp', ['3'], 'Matrix Type Received from Server:'),
    ('core_experiments/02_slang_translator_udp', ['tbh idk rn'], 'Translated Sentence:'),
    ('core_experiments/03_time_server_udp', ['stop'], 'Server reply: Server stopped.'),
    ('core_experiments/05_smtp_mail_transfer_tcp', ['alice@test.com', 'bob@test.com', 'Test Mail', 'Hello SMTP body'], '250 Email received successfully'),
    ('core_experiments/07_concurrent_file_server_multiprocess_tcp', ['sample.txt'], 'Server PID:')
]

def main():
    print("=" * 65)
    print("  COMPUTER NETWORKS SOCKET PROGRAMMING VERIFICATION SUITE")
    print("=" * 65)

    passed = 0
    failed = 0

    for folder, args, expected in TESTS:
        work_dir = os.path.join(BASE_DIR, folder)
        server_path = os.path.join(work_dir, 'server.py')
        client_path = os.path.join(work_dir, 'client.py')

        if not os.path.exists(server_path) or not os.path.exists(client_path):
            print(f"[ERROR] Missing files in {folder}")
            failed += 1
            continue

        # Launch server process
        srv_proc = subprocess.Popen(
            [sys.executable, server_path],
            cwd=work_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(0.35)

        try:
            cl_proc = subprocess.run(
                [sys.executable, client_path] + args,
                cwd=work_dir,
                capture_output=True,
                text=True,
                timeout=5
            )
            output = cl_proc.stdout + cl_proc.stderr

            if expected in output:
                print(f"[PASS] {folder.ljust(50)} -> OK")
                passed += 1
            else:
                print(f"[FAIL] {folder}")
                print(f"       Expected: {expected}")
                print(f"       Received: {output.strip()[:160]}")
                failed += 1
        except Exception as e:
            print(f"[FAIL] {folder} (Exception: {e})")
            failed += 1
        finally:
            try:
                srv_proc.terminate()
                srv_proc.wait(timeout=1)
            except Exception:
                srv_proc.kill()

    print("=" * 65)
    print(f"Summary: {passed} PASSED, {failed} FAILED out of {len(TESTS)} automated suites.")
    print("=" * 65)

    if failed > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()
