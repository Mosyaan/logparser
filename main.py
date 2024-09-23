import re
from collections import Counter
from datetime import datetime

# чтение логов
def read_log_file(file_path):
	with open(file_path, 'r') as file:
		return file.readlines()

# парсинг логов
def parse_logs(logs):
	failed_logins = []
	successful_logins = []
	sudo_uses = []

	for log in logs:
		if 'authentication failure' in log:
			failed_logins.append(log)
		elif 'systemd-logind' in log and 'New session' in log:
			successful_logins.append(log)
		elif 'sudo:' in log:
			sudo_uses.append(log)

	return failed_logins, successful_logins, sudo_uses

# генерация отчета
def generate_report(failed_logins, successful_logins, sudo_uses):
	failed = 0
	succeeded = 0
	sudo = 0

	for log in failed_logins:
		failed += 1
	for log in successful_logins:
		succeeded += 1
	for log in sudo_uses:
		sudo += 1

	print(f'Успешных входов: {succeeded}\nНеудачных входов: {failed}\nИспользование sudo: {sudo}\n')
	st = input('Сгенерировать полный отчёт? (Y/N): ').lower

	if st == 'y' or st == 'н':

		print("Неудачные попытки входа:")
		for log in failed_logins:
			print(log.strip())

		print("\nУспешные входы:")
		for log in successful_logins:
			print(log.strip())

		print("\nИспользование sudo:")
		for log in sudo_uses:
			print(log.strip())
	else:
		return


if __name__ == "__main__":
	log_file_path = "/var/log/auth.log"

	logs = read_log_file(log_file_path)

	failed_logins, successful_logins, sudo_uses = parse_logs(logs)

	if input().lower == 'yes':
		generate_report(failed_logins, successful_logins, sudo_uses)

	generate_report(failed_logins, successful_logins, sudo_uses)