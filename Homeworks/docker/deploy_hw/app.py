from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import gradio as gr
import os
import cv2
import numpy as np

# Load the model
cache_dir = os.path.dirname(os.path.realpath(__file__))
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50",
                                               revision="no_timm",
                                               cache_dir=cache_dir)
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50",
                                               revision="no_timm",
                                               cache_dir=cache_dir)


# Define the inference function
def detr_inference(image):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(
        outputs, target_sizes=target_sizes, threshold=0.9)[0]

    # Convert PIL image to OpenCV format
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Draw the bounding boxes on the image
    for score, label, box in zip(results["scores"], results["labels"],
                                 results["boxes"]):
        rand_color = np.random.randint(0, 256, size=3).tolist()
        box = [round(i, 2) for i in box.tolist()]
        cv2.rectangle(image,
                      (int(box[0]), int(box[1])),
                      (int(box[2]), int(box[3])),
                      rand_color,
                      3)
        # convert the label to the actual class name
        label = model.config.id2label[label.item()]
        cv2.putText(image, f'{label}: {score:.2f}',
                    (int(box[0]), int(box[1]) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    rand_color,
                    4)

    # Convert the image back to PIL format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    return image


# Create a Gradio interface
webui = gr.Interface(
    detr_inference,
    gr.Image(type="pil"),
    outputs=["image"],
    flagging_options=[],
)

if __name__ == "__main__":
    webui.launch(server_name="0.0.0.0", server_port=7000,
                 debug=True)
