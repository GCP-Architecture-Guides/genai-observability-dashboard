```
This is not an officially supported Google product.
This code snippet and dashboard is a logging example for GenAI guardrail observability. 
This demo code is not built for production workload. 
```

[//]: # "leesd@google.com"

# GenAI guardrail observability.

# Summary

To ensure the safe and effective deployment of generative AI applications, a system for monitoring guardrails is invaluable.  By recording prompt inputs and model responses, developers gain invaluable insights into the behavior of their LLM applications. This granular level of detail enables the identification of potential risks, the detection of prompt injection attacks, and the fine-tuning of guardrails to prevent unintended or harmful outputs. Looking at the flow of a prompt through various evaluation types, each of these layers can report data on their effectiveness to give a trend analysis on how users are interacting with the model and trends of the guardrails behavior.

![image](./images/genai_prompt_guardrails.png)


# Architecture 

Key Components

<p align="center"><img src="./images/observability_logging_architecture.png"></p>

The logging method is responsible for:
- Log Entry Creation: Generating structured log messages that capture:
	- Timestamp
	- Log Level (INFO, DEBUG, WARN, ERROR)
	- Guardrail evaluated
	- Input Parameters (optional)
	- Return Values (optional)
- Log Output: Directing log messages to the chosen destination(s) (file, console, database, etc.).
- Log Entries: The individual records containing information about method calls and their execution.

Structuring the logging payload is important to develop a dashboard that can deliver value.  
<p align="center"><img src="./images/json_payload.png"></p>
The values for the category of guardrail are defined by your usage of different guardrail methods within your application and can be combinations of checks such as combining DLP with secondary LLM evaluation. 

## Design considerations

This logging design is set to be included into your LLM applications and generate appropriate data during its execution.  It is important to place logging calls at each of the guardrail evaluation methods to capture the data from that execution. 

For example, if you were using the DLP service of Sentitive Data Protection to evaluate a prompt for PII data, you insert logging calls during that evaluation:
```
# Checking input and output with DLP
def generate_response_with_dlp(input):

    if valid_dlp_text(input):
        output=generate_answer(input)
        if valid_dlp_text(output):
            log_prompt(input, output, "DLP")
            return(output)
        else:
            log_prompt(input, "blocked", "DLP")
            return ("Sorry, I can not provide the answer.")

    else:
        return ("Please do not provide PII as input.")
```

# Deployment

Add the logging code to your LLM application.

Create a logging sink in log router for the logger that directs to a BigQuery dataset for storage.
<p align="center"><img width=400 src="./images/sink_details.png"></p>

Create a dashboard using the BigQuery dataset stream to visualize the model guardrail behaviors.
<p align="center"><img src="./images/bq_dataset_genai_observability.png"></p>

Example Looker Studio Dashboard:
<p align="center"><img width=300 src="./images/looker_studio_bashboard.png"></p>
