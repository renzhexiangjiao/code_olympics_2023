def stage_1(line):
    prompt = line[4]

    if prompt == 1:
        label = line[1]
    elif prompt == 2:
        label = line[1]
    elif prompt == 3:
        label = line[2]
    else:
        label = line[3]

    prev_stage[1] = {"position": prompt, "label": label}

    return label


def stage_2(line):
    prompt = line[4]

    if prompt == 1:
        label = 4
    elif prompt == 2:
        stage_1_pos = prev_stage[1]["position"]

        label = line[stage_1_pos]
    elif prompt == 3:
        label = line[0]
    else:
        stage_1_pos = prev_stage[1]["position"]

        label = line[stage_1_pos]

    prev_stage[2] = {"position": prompt, "label": label}

    return label


def stage_3(line):
    prompt = line[4]

    if prompt == 1:
        stage_2_label = prev_stage[2]["label"]

        label = stage_2_label
    elif prompt == 2:
        stage_1_label = prev_stage[1]["label"]

        label = stage_1_label
    elif prompt == 3:
        label = line[3]
    else:
        label = 4

    prev_stage[3] = {"position": prompt, "label": label}

    return label


def stage_4(line):
    prompt = line[4]

    if prompt == 1:
        stage_1_pos = prev_stage[1]["position"]

        label = line[stage_1_pos]
    elif prompt == 2:
        label = line[1]

    elif prompt == 3:
        stage_2_pos = prev_stage[2]["position"]

        label = line[stage_2_pos]
    else:
        stage_2_pos = prev_stage[2]["position"]

        label = line[stage_2_pos]

    prev_stage[4] = {"position": prompt, "label": label}

    return label


def stage_5(line):
    prompt = line[4]

    if prompt == 1:
        stage_1_pos = prev_stage[1]["position"]

        label = line[stage_1_pos]
    elif prompt == 2:
        stage_2_pos = prev_stage[2]["position"]

        label = line[stage_2_pos]

    elif prompt == 3:
        stage_3_pos = prev_stage[3]["position"]

        label = line[stage_3_pos]
    else:
        stage_4_pos = prev_stage[4]["position"]

        label = line[stage_4_pos]

    prev_stage[5] = {"position": prompt, "label": label}

    return label


stage = {0: stage_1, 1: stage_2, 2: stage_3, 3: stage_4, 4: stage_5}
prev_stage = {}


def decipherer(input_array):

    output_code = []
    for index, value in enumerate(input_array):
        code = str(stage[index](value))
        output_code.append(code)

    output = "".join(output_code)

    return output
