import sys
import time, os
import P_Logger
import filecmp

start_time = time.time()
divergences = []


def get_files(path):
    files = []
    for file in os.listdir(path):
        if file.__contains__(".spf") or file.__contains__(".SPF") or file.__contains__(".wzor"):
            if os.path.isfile(os.path.join(path, file)):
                files.append(os.path.join(path, file))
    return files


def compare_files(templateFile, file):
    if os.path.exists(templateFile) and os.path.exists(file):
        P_Logger.logger.info('Starting checking ...' + templateFile + " and " + file)
        # reading files
        f1 = open(templateFile, "r")
        f2 = open(file, "r")

        f1_data = f1.readlines()
        f2_data = f2.readlines()

        i = 0

        for i, line1 in enumerate(f1_data):

            # matching line1 from both files
            if f1_data[i] == f2_data[i]:
                # print IDENTICAL if similar
                print("Line ", i, ": IDENTICAL")
            else:
                print("Line ", i, ":")
                # else print that line from both files
                print("\tFile 1:", f1_data[i], end='')
                print("\tFile 2:", f2_data[i], end='')
                divergences.append(os.path.basename(file) + ": " + f1_data[i].rstrip() + " != " + f2_data[i].rstrip())

            i += 1

        # closing files
        f1.close()
        f2.close()
        return divergences


def main():
    P_Logger.logger.info('Starting checking ...')

    # check directory
    folder = r'./Source'
    if not (os.path.dirname(folder)):
        P_Logger.logger.error('brak katalogu!')
        sys.exit()

    files = get_files(folder)

    for file in files:
        P_Logger.logger.debug(file)
        compare_files(file.replace(".SPF","_wzor.SPF"), file)

    # filemaster = r"C:\Users\user\source\repos\P_CompareFiles\Source\B12345614_wzor.SPF"
    # file = r"C:\Users\user\source\repos\P_CompareFiles\Source\B12345614.SPF"
    # compare_files(filemaster, file)

    count = 1
    for item in divergences:
        if item is not None:
            P_Logger.logger.error(f'{item}')
            count += 1

    P_Logger.logger.info("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
