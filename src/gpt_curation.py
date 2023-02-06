
import openai


def evalute_enzyme(abstract):
    """
    evalaution function
    """
    # setup model and prompt
    model_engine = "text-davinci-003"
    prompt = "Based on following description, does this enzyme involve into metabolic process?\n"
    tldr_tag = "\n tl;dr:"
    combined_text = prompt + abstract + tldr_tag
    response = openai.Completion.create(
        model=model_engine,
        prompt=combined_text,
        temperature=0.7,
        max_tokens=450,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0]["text"].replace("\n", " ")

