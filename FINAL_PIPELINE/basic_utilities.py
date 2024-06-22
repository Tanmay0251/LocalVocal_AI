########################################################################################################################

# Importing necessary libraries
import google.generativeai as genai
import typing_extensions as typing
import pathlib
import json
import os
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

########## API key #####################################################################################################

with open('GEMINI_API_KEY') as f:
    os.environ['GOOGLE_API_KEY'] = f.read()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

########## text -> json ################################################################################################

def txt_to_json(text):

    '''
    Arguments:
    *text: str
    '''

    return json.loads(text)

########## text -> text ################################################################################################

def txt_to_txt(prompt, num_results=1, model='gemini-1.5-flash'):

    '''
    Arguments:
    *prompt: str
    *num_results: int
    *model: str

    Default values:
    *num_results = 1
    *model = 'gemini-1.5-flash'
    '''

    # No need to structure the output as a list
    if num_results == 1:
        response = genai.GenerativeModel(model).generate_content(prompt)
        return response.text
    
    # Structure the output as a list
    else:
        # Define the structure of the output
        class Prompts(typing.TypedDict):
            prompts: typing.List[str]
        response = genai.GenerativeModel(model).generate_content(
            prompt,
            generation_config=genai.GenerationConfig(response_mime_type="application/json",response_schema=Prompts)
        )
        # Output will still be a string in json format
        return response.text

########## image -> text ################################################################################################

def img_to_txt(prompt,image_path, model='gemini-1.0-pro-vision'):

    '''
    Arguments:
    *prompt: str
    *image_path: str
    *model: str

    Default values:
    *model = 'gemini-1.5-flash'
    '''

    # for passing image data
    image = {
        'mime_type': 'image/jpeg',
        'data': pathlib.Path(image_path).read_bytes()
    }

    response = genai.GenerativeModel(model).generate_content([prompt, image])
    return response.text

########## text -> image ################################################################################################

def txt_to_img(prompt, gcp_project_id, file_path='image.jpg', model="imagegeneration@005"):

    '''
    Arguments:
    *prompt: str
    *gcp_project_id: str
    *file_path: str
    *model: str

    Default values:
    *file_path = 'image.jpg'
    *model = "imagegeneration@005"
    '''

    gcp_project_id = gcp_project_id
    ##### NEED TO AUTHENTICATE WITH GCP ##### IMPORTANT #####
    vertexai.init(project=gcp_project_id)

    image = ImageGenerationModel.from_pretrained(model).generate_image(prompt, number_of_images=1)
    image.save(file_path)
    return file_path

########################################################################################################################