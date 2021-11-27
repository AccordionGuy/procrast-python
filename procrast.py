import os
import shutil
import sys


deny_list = [
  'facebook.com',
  'www.facebook.com',
  'twitter.com',
  'www.twitter.com',
  'linkedin.com',
  'www.reddit.com',
  'reddit.com',
]

if os.name == 'posix':
  HOSTS_FILE_PATH = '/etc/hosts'
  HOSTS_BACKUP_FILE_PATH = '/etc/hosts.bak'
else:
  HOSTS_FILE_PATH = 'c:\Windows\System32\Drivers\etc\hosts'
  HOSTS_BACKUP_FILE_PATH = 'c:\Windows\System32\Drivers\etc\hosts.bak'

IPV4_LOOPBACK_ADDRESS = '127.0.0.1'
IPV6_LOOPBACK_ADDRESS = 'fe80::1%lo0'

def block_sites():
  print("Blocking sites...")
  with open(HOSTS_FILE_PATH, 'r+') as hosts_file:
    hosts_file_content = hosts_file.read()
    for domain in deny_list:
      if domain not in hosts_file_content:
        hosts_file.write(f"{IPV4_LOOPBACK_ADDRESS} {domain}\n")
        hosts_file.write(f"{IPV6_LOOPBACK_ADDRESS} {domain}\n")
        print(f"Blocked {domain}.")
        
def back_up_hosts_file():
    print("Backing up hosts file...")
    shutil.copyfile(HOSTS_FILE_PATH, HOSTS_BACKUP_FILE_PATH)
    
def restore_hosts_file():
    print("Restoring hosts file...")
    shutil.copyfile(HOSTS_BACKUP_FILE_PATH, HOSTS_FILE_PATH)

if __name__ == '__main__':
  command_line_args = sys.argv
  command_line_args_count = len(command_line_args)
  if command_line_args_count == 2:
    option = command_line_args[1]
    if option == "block":
      back_up_hosts_file()
      block_sites()
    elif option == "unblock":
      restore_hosts_file()
    else:
      print("Use 'block' or 'unblock'.")
  else:
    print("Use the right number of commands, bucko!")
