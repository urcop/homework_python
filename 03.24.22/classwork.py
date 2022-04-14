import subprocess as sub


def main():
    command = 'ping '
    with open('servers.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        address = ' '.join(line.split(':'))
        command += address
        print(sub.getstatusoutput(command))


if __name__ == '__main__':
    main()
