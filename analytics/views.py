import os
import joblib
import pandas as pd
from django.views import View
from django.shortcuts import render
from django.utils import timezone
from diplomacy.models import ZimbabweEconomicData
from analytics.predictive import train_inflation_model, train_exchange_rate_model, save_model

class TrainModelView(View):
    template_name = 'analytics/train_model.html'

    def get(self, request):
        context = {}
        qs = ZimbabweEconomicData.objects.all().order_by('date')
        df = pd.DataFrame(list(qs.values()))
        
        if not df.empty:
            # Train inflation model
            inflation_model, inflation_params, inflation_mae, inflation_mse = train_inflation_model(df)
            # Train exchange rate model
            exchange_model, exchange_params, exchange_mae, exchange_mse = train_exchange_rate_model(df)
            
            # Ensure the directory exists for saving models
            model_dir = os.path.join(os.getcwd(), 'analytics', 'models')
            os.makedirs(model_dir, exist_ok=True)
            
            save_model(inflation_model, os.path.join(model_dir, 'best_inflation_model.joblib'))
            save_model(exchange_model, os.path.join(model_dir, 'best_exchange_model.joblib'))
            
            context['message'] = "Models trained successfully."
            context['inflation_params'] = inflation_params
            context['inflation_error'] = {'MAE': inflation_mae, 'MSE': inflation_mse}
            context['exchange_params'] = exchange_params
            context['exchange_error'] = {'MAE': exchange_mae, 'MSE': exchange_mse}
        else:
            context['message'] = "No data available for training models."
        
        return render(request, self.template_name, context)

class PredictiveAnalyticsView(View):
    template_name = 'analytics/predictive.html'
    
    def get(self, request):
        context = {}
        model_dir = os.path.join(os.getcwd(), 'analytics', 'models')
        inflation_model_path = os.path.join(model_dir, 'best_inflation_model.joblib')
        exchange_model_path = os.path.join(model_dir, 'best_exchange_model.joblib')
        
        qs = ZimbabweEconomicData.objects.all().order_by('date')
        df = pd.DataFrame(list(qs.values()))
        
        if not df.empty:
            if os.path.exists(inflation_model_path) and os.path.exists(exchange_model_path):
                inflation_model = joblib.load(inflation_model_path)
                exchange_model = joblib.load(exchange_model_path)
                
                # Use the last record for demonstration
                inflation_features = df[['central_bank_rate', 'reserve_money', 'broad_money_m3', 'official_exchange_rate', 'parallel_exchange_rate']].iloc[-1].values.reshape(1, -1)
                exchange_features = df[['broad_money_m3', 'reserve_money', 'monthly_trade_balance', 'zwg_mom_inflation', 'usd_yoy_inflation']].iloc[-1].values.reshape(1, -1)
                
                predicted_inflation = inflation_model.predict(inflation_features)[0]
                predicted_exchange = exchange_model.predict(exchange_features)[0]
                
                context['inflation_prediction'] = predicted_inflation
                context['exchange_prediction'] = predicted_exchange
                context['message'] = "Predictions generated successfully."
            else:
                context['message'] = "Models not found. Please train the models first."
        else:
            context['message'] = "No data available for predictions."
        
        return render(request, self.template_name, context)

## Chatbot view with System Messages for output regulation
import os
from django.shortcuts import render
from openai import OpenAI  # Interfaces with the NVIDIA endpoint via OpenAI API style
import mistune  # Optional: Converts Markdown to HTML

def chatbot_view(request):
    # Retrieve the NVIDIA API key from environment variables.
    nvidia_api_key = os.environ.get("NV_API_KEY", "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")
    
    # Get user input from GET parameters
    user_input = request.GET.get('user_input', '')
    response_text = ""
    
    if user_input:
        try:
            client = OpenAI(
                base_url="https://integrate.api.nvidia.com/v1",  # NVIDIA endpoint
                api_key=nvidia_api_key
            )
            # Include a system message to set context and guide responses
            messages = [
                {"role": "system", "content": (
                    "You are a neutral assistant. Do not take sides on political issues. "
                    "For visa-related queries, note that a visa is free for the first 30 days for Africans, Commonwealth Members, and Francophone Countries. "
                    "For economic questions, include a reference to the Rwanda Development Board: https://rdb.rw/"
                )},
                {"role": "user", "content": user_input}
            ]
            
            completion = client.chat.completions.create(
                model="mistralai/mixtral-8x7b-instruct-v0.1",  # New model
                messages=messages,
                temperature=0.2,
                top_p=0.7,
                max_tokens=1024,
                stream=True
            )
            
            for chunk in completion:
                if chunk.choices[0].delta.content is not None:
                    response_text += chunk.choices[0].delta.content
        except Exception as e:
            response_text = f"Error during inference: {str(e)}"
    
    # Convert Markdown to HTML
    markdown_converter = mistune.create_markdown()
    response_html = markdown_converter(response_text)
    
    context = {
        "user_input": user_input,
        "response": response_html,
    }
    return render(request, "analytics/chatbot.html", context)

# Grafana Dashboard views
def grafana_dashboard(request):
    return render(request, 'analytics/grafana_dashboard.html')

def grafana_link(request):
    return render(request, 'analytics/grafana_link.html')
