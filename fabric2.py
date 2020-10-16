import sys
import os
from fabric import Connection
from termcolor import colored
# global is_migrated_on_server

try:
	from creds1 import *
except ImportError:
	print("provide all neccasary vars")
	exit()

'''
	branch name must be in last
'''

def deploy(conn, collect_static='y', install_reqs='y', migrate='y', restart_nginx='n', restart_server='n', branch=assigned_branch):

	collect_static = (collect_static == 'y')
	install_reqs = (install_reqs == 'y')
	migrate = (migrate == 'y')
	restart_server = (restart_server == 'y')
	restart_nginx = (restart_nginx == 'y')

	if branch != assigned_branch:
		print(branch, assigned_branch)
		sys.stderr.write('Only master can be deployed on prod server')
		return
	else:
		print(colored("Deploying: %s on %s" %(branch, conn.host), "green"))

	with conn.cd(code_dir_master):
		print(colored("Found Code Directory: %s" %(code_dir_master), "green"))

		conn.run("sudo git checkout -f")
		conn.run("sudo git checkout {}".format(branch))

		if conn.host and assigned_branch==branch:
			repo_url = "https://%s:%s@gitlab.com/%s/%s.git %s" %(git_user, git_password, repo_maintner, service_name, branch)
			conn.run("sudo git pull " + repo_url+" --no-edit")
		else:
			sys.stderr.write('Select the correct deployment machine')
			return

		print(colored("Deleting Pyc files..", "green"))
		conn.run("find . -name '*.pyc' -delete")
		print(colored("Deleted Pyc files..", "green"))

		# code to check migrations
		# is_migrated_on_server = 0
		# if is_migrated_on_server == 0:
		# 	num_migrations = conn.run("python3 manage.py showmigrations --list | grep '\[ ] ' | wc -l")
		# 	print("num_migrations", num_migrations)
		# 	if num_migrations and not num_migrations.startswith("Command exited with status 0"):
		# 		print(colored("We have pending migrations... migrating now", "green"))
		# 		migrate = True


		if install_reqs:
			req_txt_file = new_requirements_txt_file_name or "requirements.txt"
			print(colored("Installing Requirements..", "green"))
			conn.run("sudo pip3 install -r %s"%(req_txt_file))

		if collect_static:
			print(colored("Collecting Static Files..", "green"))
			conn.run("python3 manage.py collectstatic --noinput")
			print(colored("Collected successfully static Files..", "green"))

		if migrate:
			print(colored("Starting Migrations..", "green"))
			conn.run("python3 manage.py migrate")
			print(colored("Migrations done..", "green"))
			# is_migrated_on_server = 1

		if restart_server:
			print(colored("Restarting service ..", "green"))
			conn.run('sudo supervisorctl status %s | sed "s/.*[pid ]\\([0-9]\\+\\)\\,.*/\\1/" | xargs kill -HUP'%(service_name))

		if restart_nginx:
			print(colored("Restarting nginx..", "green"))
			conn.run("sudo service nginx restart")

		print(colored("Code Deployed Successfully :D", "green"))


def stop_all_management_commands(conn, host, branch_allowed_for_management_command):

	if branch_allowed_for_management_command!=assigned_branch:
		print(colored("Branch Inconsistency between user-input-provided and assigned", "red"))
		return

	print(colored("Stopping all management commands..", "red"))

	if host_mapping_management_handler.get(host):
		stopped_host_services = host_mapping_management_handler.get(host)

	else:
		print(colored("No management services found in host assignments", "green"))
		return

	for service in stopped_host_services:
		conn.run("sudo supervisorctl stop %s"%(service))
		print(colored("Stopped %s"%(service), "green"))

	print(colored("Stopped all management commands..", "green"))


def start_all_management_commands(conn, host, branch_allowed_for_management_command):

	if branch_allowed_for_management_command!=assigned_branch:
		print(colored("Branch Inconsistency between user-input-provided and assigned", "red"))
		return

	print(colored("Starting all management commands..", "red"))

	if host_mapping_management_handler.get(host):
		to_start_host_services = host_mapping_management_handler.get(host)
	else:
		print(colored("No management services found in host assignments", "green"))
		return


	for service in to_start_host_services:
		conn.run("sudo supervisorctl start %s"%(service))
		print(colored("Started %s"%(service), "green"))
	else:
		print(colored("No management services found in host assignments", "green"))
		return


	print(colored("Started all management commands..", "green"))

def main():

	if len(sys.argv)<=1:
		print("please provide vaild param for collect_static:install_reqs:migrate:restart_nginx:restart_server in format of y:n:n:n format")
		return

	deploy_rules= sys.argv[1].split(":")
	branch_allowed_for_management_command = assigned_branch #deploy_rules[-1]

	for host, user, pem in zip(hosts, users, pem_files):

		conn = Connection(inline_ssh_env=pem, host=host, user=user, connect_kwargs={ "key_filename": pem})

		# if management_command_transaction_enabled:
		# 	stop_all_management_commands(conn, host, branch_allowed_for_management_command)

		deploy(conn, *deploy_rules)

		# if management_command_transaction_enabled:
		# 	start_all_management_commands(conn, host, branch_allowed_for_management_command)


main()
