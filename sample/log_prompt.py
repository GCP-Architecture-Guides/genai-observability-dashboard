##  Copyright 2024 Google LLC
##  
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##  
##      https://www.apache.org/licenses/LICENSE-2.0
##  
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.


##  This code snippet creates a logging function using Cloud Logging that can  ##
##  be included in a python notebook or application to log GenAI Prompt behavior ##
##  This demo code is not built for production workload ##

#@title Log Function

def log_prompt(prompt_in, model_out, category):

  # Imports the Cloud Logging client library
  import google.cloud.logging
  import logging

  if model_out == "blocked":
     is_blocked = "denied"
  else:
     is_blocked = "allowed"

  client = google.cloud.logging.Client()
  logger = client.logger("genai_prompt_observability")

  # Emits the data using the standard logging module
  logger.log_struct(
      {
          "prompt": prompt_in,
          "response": model_out,
          "blocked": is_blocked,
          "safety scores": "",
          "category": category
      },
      severity="INFO",
  )
