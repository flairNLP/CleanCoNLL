import csv, os

PATH_REISS = "../data/reiss2020_conll/"

PATH_ANNOTATIONS = "../data/ruecker2023_annotations/"
PATH_TARGET = "../data/corpus/"


def combine_conll_files(path_reiss, path_annotations, path_output):

    for k, (file1, file2) in {"train": ("eng.train", "conll.train"),
                              "dev": ("eng.testa", "conll.dev"),
                              "test": ("eng.testb", "conll.test")}.items():

        # Read in the first file with Reiss version
        with open(path_reiss + file1, 'r') as f:
            reader = csv.reader(f, delimiter=' ', quoting = csv.QUOTE_NONE)
            reiss_data = [row for row in reader]

        # Read in the second file with masked tokens and Clean Conll annotations
        with open(path_annotations + file2, 'r') as f:
            reader = csv.reader(f, delimiter='\t', quoting = csv.QUOTE_NONE)
            annotations_data = [row for row in reader]

        # Make sure the two files have same number of lines
        assert len(reiss_data) == len(annotations_data), f"It seems as the two files ({k} split) don't have the same number of lines."

        # Combine the data from both files
        combined_data = []
        for i in range(len(reiss_data)):
            if len(reiss_data[i]) == 0:
                combined_row = [""]
            else:
                combined_row = [reiss_data[i][0]] + annotations_data[i][1:]
            #print(combined_row)
            combined_data.append(combined_row)

        # Write the combined data to the output file and creating Clean Conll
        if not os.path.exists(path_output):
            os.makedirs(path_output)

        with open(path_output + f"clean_conll.{k}", 'w') as f:
            for data in combined_data:
                line = "\t".join(data)
                f.write(line)
                f.write('\n')



combine_conll_files(path_reiss = PATH_REISS,
                    path_annotations = PATH_ANNOTATIONS,
                    path_output = PATH_TARGET
                    )


