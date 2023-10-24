import csv, os, json

PATH_REISS = "../data/reiss2020_conll/"

PATH_ANNOTATIONS = "../data/CleanCoNLL_annotations/"
PATH_LINEBREAK_CHANGES = "../data/CleanCoNLL_linebreak_changes/"
PATH_TARGET = "../data/CleanCoNLL_corpus/"


def combine_conll_files(path_reiss, path_annotations, path_linebreaks, path_output):

    for k, (file1, file2, linebreak_file) in {"train": ("eng.train", "cleanconll_annotations.train", "train.json"),
                                              "dev": ("eng.testa", "cleanconll_annotations.dev", "dev.json"),
                                              "test": ("eng.testb", "cleanconll_annotations.test", "test.json")}.items():

        # Read in the first file: CoNLL version by Reiss et al. (2020)
        with open(path_reiss + file1, 'r') as f:
            reader = csv.reader(f, delimiter=' ', quoting = csv.QUOTE_NONE)
            reiss_data = [row for row in reader]

        # Read in the second file: the CleanCoNLL annotations with masked tokens ([TOKEN])
        with open(path_annotations + file2, 'r') as f:
            reader = csv.reader(f, delimiter='\t', quoting = csv.QUOTE_NONE)
            annotations_data = [row for row in reader]

        # Read in the third file: with linebreak changes from Reiss to CleanCoNLL
        with open(path_linebreaks + linebreak_file, 'r') as f:
            linebreaks = json.load(f)


        # Combine the data from the three files
        combined_data = []
        line_num_reiss = 0
        line_num_cleanconll = 0
        while line_num_reiss <len(reiss_data):
            if str(line_num_reiss) in linebreaks.keys():
                reiss_tokens = linebreaks[str(line_num_reiss)]["original_reiss_tokens"]
                cleanconll_tokens = linebreaks[str(line_num_reiss)]["cleanconll_tokens"]
                for i, t in enumerate(cleanconll_tokens):
                    combined_row = [t] + annotations_data[line_num_cleanconll][1:]
                    print(combined_row)
                    combined_data.append(combined_row)
                    line_num_cleanconll +=1
                line_num_reiss +=1

            else:
                if len(reiss_data[line_num_reiss]) == 0:
                    combined_row = [""]
                else:
                    combined_row = [reiss_data[line_num_reiss][0]] + annotations_data[line_num_cleanconll][1:]
                print(combined_row)
                combined_data.append(combined_row)
                line_num_reiss +=1
                line_num_cleanconll +=1

        # Write the combined data to the output file and create CleanCoNLL output files
        if not os.path.exists(path_output):
            os.makedirs(path_output)

        with open(path_output + f"cleanconll.{k}", 'w') as f:
            for data in combined_data:
                line = "\t".join(data)
                f.write(line)
                f.write('\n')



combine_conll_files(path_reiss = PATH_REISS,
                    path_annotations = PATH_ANNOTATIONS,
                    path_output = PATH_TARGET,
                    path_linebreaks= PATH_LINEBREAK_CHANGES,
                    )


