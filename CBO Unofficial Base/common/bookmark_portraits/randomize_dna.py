import os
import re
import random

for file in os.listdir(os.curdir):
    filename = os.fsdecode(file)
    if not filename.endswith(".txt"): 
        continue
    with open(file, "r") as f:
        old_lines = f.readlines()
        
    random.seed()
        
    new_lines = []
    for line in old_lines:
        if "gene_bs_penis_size" in line or \
           "gene_bs_penis_thickness" in line or \
           "gene_bs_ball_size" in line or \
           "gene_bs_butt_size" in line or \
           "gene_bs_body_fat_distribution" in line or \
           "gene_bs_upper_body_muscle" in line or \
           "gene_bs_lower_body_muscle" in line or \
           "gene_muscle_definition" in line or \
           "gene_bs_nipples" in line or \
           "gene_areolas" in line or \
           "gene_bs_hips" in line or \
           "gene_bs_shoulders" in line or \
           "gene_bs_waist" in line or \
           "gene_bs_shrink_bookmark" in line:
           continue
        if "gene_bs_body_type" in line:
            new_lines.append(line)
            weight = int(re.search(r'\d+', line)[0])

            # Distribution based on ethnicities_portraits
            penis_size_index = random.randint(1, 48)
            penis_size = 0.0
            if penis_size_index <= 5:
                penis_size = random.uniform(0.00, 0.14)
            elif penis_size_index <= 16:
                penis_size = random.uniform(0.14, 0.28)
            elif penis_size_index <= 29:
                penis_size = random.uniform(0.28, 0.42)
            elif penis_size_index <= 40:
                penis_size = random.uniform(0.42, 0.58)
            elif penis_size_index <= 45:
                penis_size = random.uniform(0.58, 0.72)
            elif penis_size_index <= 47:
                penis_size = random.uniform(0.72, 0.86)
            else:
                penis_size = random.uniform(0.86, 1.00)

            penis_thickness_index = random.randint(1, 48)
            penis_thickness = 0.0
            if penis_thickness_index <= 5:
                penis_thickness = random.uniform(0.00, 0.14)
            elif penis_thickness_index <= 16:
                penis_thickness = random.uniform(0.14, 0.28)
            elif penis_thickness_index <= 29:
                penis_thickness = random.uniform(0.28, 0.42)
            elif penis_thickness_index <= 40:
                penis_thickness = random.uniform(0.42, 0.58)
            elif penis_thickness_index <= 45:
                penis_thickness = random.uniform(0.58, 0.72)
            elif penis_thickness_index <= 47:
                penis_thickness = random.uniform(0.72, 0.86)
            else:
                penis_thickness = random.uniform(0.86, 1.00)

            ball_size_index = random.randint(1, 48)
            ball_size = 0.0
            if ball_size_index <= 5:
                ball_size = random.uniform(0.00, 0.14)
            elif ball_size_index <= 16:
                ball_size = random.uniform(0.14, 0.28)
            elif ball_size_index <= 29:
                ball_size = random.uniform(0.28, 0.42)
            elif ball_size_index <= 40:
                ball_size = random.uniform(0.42, 0.58)
            elif ball_size_index <= 45:
                ball_size = random.uniform(0.58, 0.72)
            elif ball_size_index <= 47:
                ball_size = random.uniform(0.72, 0.86)
            else:
                ball_size = random.uniform(0.86, 1.00)

            butt_size_index = random.randint(1, 48)
            butt_size = 0.0
            if butt_size_index <= 5:
                butt_size = random.uniform(0.00, 0.14)
            elif butt_size_index <= 16:
                butt_size = random.uniform(0.14, 0.28)
            elif butt_size_index <= 29:
                butt_size = random.uniform(0.28, 0.42)
            elif butt_size_index <= 40:
                butt_size = random.uniform(0.42, 0.58)
            elif butt_size_index <= 45:
                butt_size = random.uniform(0.58, 0.72)
            elif butt_size_index <= 47:
                butt_size = random.uniform(0.72, 0.86)
            else:
                butt_size = random.uniform(0.86, 1.00)

            hips_size_index = random.randint(1, 48)
            hips_size = 0.0
            if hips_size_index <= 5:
                hips_size = random.uniform(0.00, 0.14)
            elif hips_size_index <= 16:
                hips_size = random.uniform(0.14, 0.28)
            elif hips_size_index <= 29:
                hips_size = random.uniform(0.28, 0.42)
            elif hips_size_index <= 40:
                hips_size = random.uniform(0.42, 0.58)
            elif hips_size_index <= 45:
                hips_size = random.uniform(0.58, 0.72)
            elif hips_size_index <= 47:
                hips_size = random.uniform(0.72, 0.86)
            else:
                hips_size = random.uniform(0.86, 1.00)

            nipples_size_index = random.randint(1, 53)
            nipples_size = 0.0
            if nipples_size_index <= 2:
                nipples_size = random.uniform(0.00, 0.14)
            elif nipples_size_index <= 4:
                nipples_size = random.uniform(0.14, 0.28)
            elif nipples_size_index <= 14:
                nipples_size = random.uniform(0.28, 0.42)
            elif nipples_size_index <= 40:
                nipples_size = random.uniform(0.42, 0.58)
            elif nipples_size_index <= 50:
                nipples_size = random.uniform(0.58, 0.72)
            elif nipples_size_index <= 52:
                nipples_size = random.uniform(0.72, 0.86)
            else:
                nipples_size = random.uniform(0.86, 1.00)

            shoulders_size_index = random.randint(1, 53)
            shoulders_size = 0.0
            if shoulders_size_index <= 2:
                shoulders_size = random.uniform(0.00, 0.14)
            elif shoulders_size_index <= 4:
                shoulders_size = random.uniform(0.14, 0.28)
            elif shoulders_size_index <= 14:
                shoulders_size = random.uniform(0.28, 0.42)
            elif shoulders_size_index <= 40:
                shoulders_size = random.uniform(0.42, 0.58)
            elif shoulders_size_index <= 50:
                shoulders_size = random.uniform(0.58, 0.72)
            elif shoulders_size_index <= 52:
                shoulders_size = random.uniform(0.72, 0.86)
            else:
                shoulders_size = random.uniform(0.86, 1.00)

            waist_size_index = random.randint(1, 53)
            waist_size = 0.0
            if waist_size_index <= 2:
                waist_size = random.uniform(0.00, 0.14)
            elif waist_size_index <= 4:
                waist_size = random.uniform(0.14, 0.28)
            elif waist_size_index <= 14:
                waist_size = random.uniform(0.28, 0.42)
            elif waist_size_index <= 40:
                waist_size = random.uniform(0.42, 0.58)
            elif waist_size_index <= 50:
                waist_size = random.uniform(0.58, 0.72)
            elif waist_size_index <= 52:
                waist_size = random.uniform(0.72, 0.86)
            else:
                waist_size = random.uniform(0.86, 1.00)
                
            areolas_index = random.randint(1, 79)
            if areolas_index <= 17:
                areolas_index = 0
            elif areolas_index <= 49:
                areolas_index = 0
            elif areolas_index <= 65:
                areolas_index = 1
            elif areolas_index <= 73:
                areolas_index = 2
            elif areolas_index <= 77:
                areolas_index = 3
            elif areolas_index <= 79:
                areolas_index = 4
            else:
                areolas_index = 5

            penis_size_int = round(penis_size * 255.0)
            penis_thickness_int = round(penis_thickness * 255.0)
            ball_size_int = round(ball_size * 255.0)
            butt_size_int = round(butt_size * 255.0)
            hips_size_int = round(hips_size * 255.0)
            nipples_size_int = round(nipples_size * 255.0)
            shoulders_size_int = round(shoulders_size * 255.0)
            waist_size_int = round(waist_size * 255.0)

            new_lines.append("	 		gene_bs_penis_size={ \"penis_size\" %d \"penis_size\" %d }\n" % (penis_size_int, penis_size_int))
            new_lines.append("	 		gene_bs_penis_thickness={ \"penis_thickness\" %d \"penis_thickness\" %d }\n" % (penis_thickness_int, penis_thickness_int))
            new_lines.append("	 		gene_bs_ball_size={ \"ball_size\" %d \"ball_size\" %d }\n" % (ball_size_int, ball_size_int))
            new_lines.append("	 		gene_bs_butt_size={ \"butt_size\" %d \"butt_size\" %d }\n" % (butt_size_int, butt_size_int))
            new_lines.append("	 		gene_bs_nipples={ \"nipples\" %d \"nipples\" %d }\n" % (nipples_size_int, nipples_size_int))
            new_lines.append("	 		gene_bs_hips={ \"hips\" %d \"hips\" %d }\n" % (hips_size_int, hips_size_int))
            new_lines.append("	 		gene_bs_shoulders={ \"shoulders\" %d \"shoulders\" %d }\n" % (shoulders_size_int, shoulders_size_int))
            new_lines.append("	 		gene_bs_waist={ \"waist\" %d \"waist\" %d }\n" % (waist_size_int, waist_size_int))
            new_lines.append("	 		gene_areolas={ \"areolas_%d\" 0 \"areolas_%d\" 0 }\n" % (areolas_index, areolas_index))
            new_lines.append("			gene_bs_body_fat_distribution={ \"body_mid\" %d \"body_mid\" %d }\n" % (weight, weight))
            new_lines.append("			gene_bs_upper_body_muscle={ \"upper_body_muscle\" 0 \"upper_body_muscle\" 0 }\n")
            new_lines.append("			gene_bs_lower_body_muscle={ \"lower_body_muscle\" 0 \"lower_body_muscle\" 0 }\n")
            new_lines.append("			gene_muscle_definition={ \"body_muscle_definition\" 0 \"body_muscle_definition\" 0 }\n")
            new_lines.append("			gene_bs_shrink_bookmark={ \"shrink_bookmark\" 255 \"shrink_bookmark\" 255 }\n")
            continue
        new_lines.append(line)

    with open(file, "w") as f:
        f.writelines(new_lines)
