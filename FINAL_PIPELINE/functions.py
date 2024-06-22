# Description: This file contains all the functions that are used in the pipeline to generate content for the business

# importing base utilities from basic_utilities.py
import basic_utilities as basic

##############################################################################################################################
#   |  Use-case     |             function name              |                           Application                         #
##############################################################################################################################
# 1 | Image         | interpret_image_with_AI                | During post creation, interpret image into text and then      |
#   | Interpretation|                                        | forward that text to generate post description                |
#   |               |                                        |                                                               |
# 2 | Text          | enhance_business_overview_with_AI      | Use whatever business description user provides and then      |
#   | Refinement    |                                        | convert into better description                               |
#   |               |                                        |                                                               |
# 3 | Text          | enhance_post_caption_with_AI           | Use whatever post description user provides and then convert  |
#   | Refinement    |                                        | into better description                                       |
#   |               |                                        |                                                               |
# 4 | Image Prompt  | suggest_AI_img_prompt_for_profile_     | Use AI enhanced business decription to generate 3-4 image     |
#   | Generation    | gallery                                | generation prompts.                                           |
#   |               |                                        |                                                               |
# 5 | Image Prompt  | suggest_AI_img_prompt_for_profile_     | Use AI enhanced business desciption to generate 3-4 image     |
#   | Generation    | logo                                   | generation prompts for business logo image.                   |
#   |               |                                        |                                                               |
# 6 | Image Prompt  | suggest_AI_img_prompt_for_post         | Use AI enhanced post description to generate 1 image          |
#   | Generation    |                                        | generation prompt.                                            |
#   |               |                                        |                                                               |
# 7 | Image         | enhance_profile_gallery_with_AI        | Generate image for business profile gallery after profile is  |
#   | Generation    |                                        | created and send as suggestions                               |
#   |               |                                        |                                                               |
# 8 | Image         | enhance_profile_logo_with_AI           | Generate business logo from prompts and then send them as     |
#   | Generation    |                                        | notification                                                  |
#   |               |                                        |                                                               |
# 9 | Image         | enhance_post_img_with_AI               | After user has generated a post with some image, post-process |
#   | Generation    |                                        | on the backend to generate a better image for the same post   |
#   |               |                                        | and send back to business as notification. User can save the  |
#   |               |                                        | image in gallery and reuse later                              |
##############################################################################################################################

 
##############################################################################################################################
# ---------------------------------------------------- IMAGE INTERPRETATION ------------------------------------------------ #
##############################################################################################################################

def interpret_image_with_AI(prompt, image_path):

    '''
    Arguments:
    *prompt: str
    *image_path: str

    Return:
    *str

    Application:
    During post creation, interpret image into text and then forward that text to generate post description
    '''

    return basic.img_to_txt(prompt, image_path)

##############################################################################################################################
# ------------------------------------------------------- TEXT REFINEMENT -------------------------------------------------- #
##############################################################################################################################

def enhance_business_overview_with_AI(prompt,**kwargs):

    '''
    Arguments:
    *prompt: str
    *kwargs: dict

    Return:
    *str

    Application:
    Use whatever business description user provides and then convert into better description
    '''

    prompt = prompt.format(**kwargs)
    return basic.txt_to_txt(prompt)

def enhance_post_caption_with_AI(prompt,**kwargs):

    '''
    Arguments:
    *prompt: str
    *kwargs: dict

    Return:
    *str

    Application:
    Use whatever post description user provides and then convert into better description
    '''

    prompt = prompt.format(**kwargs)
    return basic.txt_to_txt(prompt)

##############################################################################################################################
# --------------------------------------------------- IMAGE PROMPT GENERATION ---------------------------------------------- #
##############################################################################################################################

def suggest_AI_img_prompt_for_profile_gallery(prompt, number_of_prompts, **kwargs):

    '''
    Arguments:
    *prompt: str
    *number_of_prompts: int
    *kwargs: dict

    Return:
    *list of str

    Application:
    Use AI enhanced business decription to generate 3-4 image generation prompts.
    '''

    prompt = prompt.format(**kwargs, number_of_prompts=number_of_prompts)
    json_out = basic.txt_to_json(basic.txt_to_txt(prompt, number_of_prompts))
    return json_out['prompts']

def suggest_AI_img_prompt_for_profile_logo(prompt, number_of_prompts, **kwargs):

    '''
    Arguments:
    *prompt: str
    *number_of_prompts: int
    *kwargs: dict

    Return:
    *list of str

    Application:
    Use AI enhanced business desciption to generate 3-4 image generation prompts for business logo image.
    '''

    prompt = prompt.format(**kwargs, number_of_prompts=number_of_prompts)
    json_out = basic.txt_to_json(basic.txt_to_txt(prompt, number_of_prompts))
    return json_out['prompts']

def suggest_AI_img_prompt_for_post(prompt, **kwargs):

    '''
    Arguments:
    *prompt: str
    *kwargs: dict

    Return:
    *str

    Application:
    Use AI enhanced post description to generate 1 image generation prompt.
    '''

    prompt = prompt.format(**kwargs)
    return basic.txt_to_txt(prompt)

##############################################################################################################################
# ------------------------------------------------------- IMAGE GENERATION ------------------------------------------------- #
##############################################################################################################################

def enhance_profile_gallery_with_AI(prompt, gcp_project_id, file_path, **kwargs):

    '''
    Arguments:
    *prompt: str
    *gcp_project_id: str
    *file_path: str
    *kwargs: dict

    Return:
    *str -> image file path

    Application:
    generate image for business profile gallery after profile is created and send as suggestions
    '''

    prompt = prompt.format(**kwargs)
    return basic.txt_to_img(prompt, gcp_project_id, file_path)

def enhance_profile_logo_with_AI(prompt, gcp_project_id, file_path, **kwargs):

    '''
    Arguments:
    *prompt: str
    *gcp_project_id: str
    *file_path: str
    *kwargs: dict

    Return:
    *str -> image file path

    Application:
    Generate business logo from prompts and then send them as notification
    '''

    prompt = prompt.format(**kwargs)
    return basic.txt_to_img(prompt, gcp_project_id, file_path)

def enhance_post_img_with_AI(prompt, gcp_project_id, file_path, **kwargs):

    '''
    Arguments:
    *prompt: str
    *gcp_project_id: str
    *file_path: str
    *kwargs: dict

    Return:
    *str -> image file path

    Application:
    After user has generated a post with some image, post-process on the backend to generate a better image for
    the same post and send back to business as notification. User can save the image in gallery and reuse later
    '''

    prompt = prompt.format(**kwargs)
    return basic.txt_to_img(prompt, gcp_project_id, file_path)

##############################################################################################################################
# ------------------------------------------------ x - x - x - x - x - x --------------------------------------------------- #
##############################################################################################################################