# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # */AIPND-revision/intropyproject-classify-pet-images/print_results.py
# #                                                                             
# # PROGRAMMER: Millicent Auma Omondi
# # DATE CREATED: 12/11/2024
# # REVISED DATE: 13/11/2024
# # PURPOSE: Create a function print_results that prints the results statistics
# #          from the results statistics dictionary (results_stats_dic). It 
# #          should also allow the user to be able to print out cases of misclassified
# #          dogs and cases of misclassified breeds of dog using the Results 
# #          dictionary (results_dic).  
# #         This function inputs:
# #            -The results dictionary as results_dic within print_results 
# #             function and results for the function call within main.
# #            -The results statistics dictionary as results_stats_dic within 
# #             print_results function and results_stats for the function call within main.
# #            -The CNN model architecture as model wihtin print_results function
# #             and in_arg.arch for the function call within main. 
# #            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
# #             print_results function and set as either boolean value True or 
# #             False in the function call within main (defaults to False)
# #            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
# #             print_results function and set as either boolean value True or 
# #             False in the function call within main (defaults to False)
# #         This function does not output anything other than printing a summary
# #         of the final results.
# ##
# # TODO 6: Define print_results function below, specifically replace the None
# #       below by the function definition of the print_results function. 
# #       Notice that this function doesn't to return anything because it  
# #       prints a summary of the results using results_dic and results_stats_dic
# # 
# def print_results(results_dic, results_stats_dic, model, 
#                   print_incorrect_dogs = False, print_incorrect_breed = False):
#     """
#     Prints summary results on the classification and then prints incorrectly 
#     classified dogs and incorrectly classified dog breeds if user indicates 
#     they want those printouts (use non-default values)
#     Parameters:
#       results_dic - Dictionary with key as image filename and value as a List 
#              (index)idx 0 = pet image label (string)
#                     idx 1 = classifier label (string)
#                     idx 2 = 1/0 (int)  where 1 = match between pet image and 
#                             classifer labels and 0 = no match between labels
#                     idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
#                             0 = pet Image 'is-NOT-a' dog. 
#                     idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
#                             'as-a' dog and 0 = Classifier classifies image  
#                             'as-NOT-a' dog.
#       results_stats_dic - Dictionary that contains the results statistics (either
#                    a  percentage or a count) where the key is the statistic's 
#                      name (starting with 'pct' for percentage or 'n' for count)
#                      and the value is the statistic's value 
#       model - Indicates which CNN model architecture will be used by the 
#               classifier function to classify the pet images,
#               values must be either: resnet alexnet vgg (string)
#       print_incorrect_dogs - True prints incorrectly classified dog images and 
#                              False doesn't print anything(default) (bool)  
#       print_incorrect_breed - True prints incorrectly classified dog breeds and 
#                               False doesn't print anything(default) (bool) 
#     Returns:
#            None - simply printing results.
#     """    
#      # Print the summary of the results statistics
#     print(f"Summary of Classification Results using {model.upper()} CNN model:")
#     print("-" * 60)
    
#     for key, value in results_stats_dic.items():
#         print(f"{key.replace('_', ' ').title()}: {value}")
    
#     print("-" * 60)
    
#     # Print incorrectly classified dogs if the flag is set to True
#     if print_incorrect_dogs:
#         print("\nIncorrectly Classified Dogs:")
#         print("-" * 30)
#         for filename, label_list in results_dic.items():
#             if label_list[3] == 1 and label_list[4] == 0:  # Dog is misclassified
#                 print(f"Image: {filename}, Pet Label: {label_list[0]}, Classifier Label: {label_list[1]}")
#         print("-" * 30)
    
#     # Print incorrectly classified breeds if the flag is set to True
#     if print_incorrect_breed:
#         print("\nIncorrectly Classified Dog Breeds:")
#         print("-" * 30)
#         for filename, label_list in results_dic.items():
#             if label_list[3] == 1 and label_list[4] == 1 and label_list[0] != label_list[1]:
#                 print(f"Image: {filename}, Pet Label: {label_list[0]}, Classifier Label: {label_list[1]}")
#         print("-" * 30)
  
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values).
    """
    # Prints summary statistics over the run
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    
    # Print the number of non-dog images
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))

    # Prints summary statistics (percentages) on Model Run
    print(" ")
    for key in results_stats_dic:
        if key.startswith('pct'):
            print("{:20}: {:.2f}%".format(key.replace('_', ' ').title(), results_stats_dic[key]))

    # IF print_incorrect_dogs == True AND there were images incorrectly 
    # classified as dogs or vice versa - print out these cases
    if (print_incorrect_dogs and 
        (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images'])):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        
        for key in results_dic:
            # Pet label is a dog and classifier says it's NOT a dog
            if results_dic[key][3] == 1 and results_dic[key][4] == 0:
                print(f"Image: {key}, Pet Label: {results_dic[key][0]}, Classifier Label: {results_dic[key][1]}")
            
            # Pet label is NOT a dog and classifier says it's a dog
            if results_dic[key][3] == 0 and results_dic[key][4] == 1:
                print(f"Image: {key}, Pet Label: {results_dic[key][0]}, Classifier Label: {results_dic[key][1]}")

    # IF print_incorrect_breed == True AND there were dogs whose breeds 
    # were incorrectly classified - print out these cases
    if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])):
        print("\nINCORRECT Dog Breed Assignment:")

        for key in results_dic:
            # Pet Image Label is a dog and is misclassified as the wrong breed
            if (results_dic[key][3] == 1 and  # It's a dog
                results_dic[key][2] == 0):  # It's misclassified
                print(f"Real: {results_dic[key][0]:>26}   Classifier: {results_dic[key][1]:>30}")              