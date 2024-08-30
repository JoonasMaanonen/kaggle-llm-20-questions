import outlines
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


class Bot:
    def __init__(self, model_dir: str, temperature: float = 0.8, device: str = "cuda") -> None:
        self.model_dir = model_dir
        self.device = device
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
        )
        llm = AutoModelForCausalLM.from_pretrained(
            model_dir,
            device_map=device,
            torch_dtype=torch.bfloat16,
            attn_implementation="eager",
            quantization_config=bnb_config,
            output_attentions=True,
            # temperature=temperature,
            do_sample=False,
        )
        tokenizer = AutoTokenizer.from_pretrained(model_dir, device_map=device)
        self.model = outlines.models.Transformers(llm, tokenizer)
