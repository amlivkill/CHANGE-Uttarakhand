import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime

@anvil.server.callable
def get_crop_recommendation(soil_type, rainfall, altitude, season):
    """AI Crop Recommendation System"""
    # Base recommendations based on Uttarakhand conditions
    recommendations = {
        'primary_crops': [
            'Manduwa (Finger Millet) - High nutrition value',
            'Jhangora (Barnyard Millet) - Drought resistant', 
            'Rajma (Kidney Beans) - Good market demand'
        ],
        'secondary_crops': [
            'Organic Vegetables - For local markets',
            'Medicinal Herbs - High value addition'
        ],
        'advisory': 'Use organic manure and practice crop rotation. Implement drip irrigation for water efficiency.'
    }
    
    # Customize based on inputs
    if "Mountain" in soil_type or "Highland" in altitude:
        recommendations['primary_crops'].append('Chaulai (Amaranth) - Hardy crop')
    
    if "Low" in rainfall:
        recommendations['advisory'] += ' Consider drought-resistant varieties and water conservation techniques.'
    
    return recommendations

@anvil.server.callable 
def calculate_water_usage(crop_area, crop_type, irrigation_type):
    """Water Management Calculator"""
    base_water = crop_area * 1500  # liters per day per hectare
    
    if irrigation_type == "Drip Irrigation":
        water_saved = base_water * 0.4
        efficiency = "High (40% savings)"
    elif irrigation_type == "Sprinkler System":
        water_saved = base_water * 0.25
        efficiency = "Medium (25% savings)"
    else:
        water_saved = base_water * 0.1
        efficiency = "Low (10% savings)"
    
    return {
        'current_usage': base_water,
        'savings': water_saved,
        'efficiency': efficiency
    }

@anvil.server.callable
def calculate_carbon_credits(land_area, farming_practice, trees_planted, practice_years):
    """Carbon Credit Income Calculator"""
    # Base calculations
    base_credits = land_area * 2  # 2 credits per hectare
    tree_credits = trees_planted * 0.1  # 0.1 credits per tree
    practice_bonus = practice_years * 0.5  # Bonus for sustained practice
    
    # Practice multiplier
    practice_multipliers = {
        "Conventional Farming": 1.0,
        "Organic Farming": 1.2, 
        "Conservation Agriculture": 1.5,
        "Agroforestry": 1.8,
        "Natural Farming": 2.0
    }
    
    multiplier = practice_multipliers.get(farming_practice, 1.0)
    
    total_credits = (base_credits + tree_credits + practice_bonus) * multiplier
    credit_value = 15  # $ per credit
    income = total_credits * credit_value
    
    return {
        'total_credits': total_credits,
        'income': income,
        'credit_value': credit_value
    }

@anvil.server.callable
def save_contact_form(name, email, phone, interest, message):
    """Save contact form data to database"""
    try:
        app_tables.contacts.add_row(
            name=name,
            email=email,
            phone=phone,
            interest=interest,
            message=message,
            created=datetime.datetime.now()
        )
        return True
    except Exception as e:
        print(f"Error saving contact: {e}")
        return False

@anvil.server.callable
def log_ai_query(query_type, parameters, result):
    """Log AI query for analytics"""
    try:
        app_tables.ai_queries.add_row(
            query_type=query_type,
            parameters=parameters,
            result=result,
            created=datetime.datetime.now()
        )
        return True
    except Exception as e:
        print(f"Error logging AI query: {e}")
        return False

@anvil.server.callable
def get_climate_data():
    """Get climate statistics for Uttarakhand"""
    return {
        'total_disasters': 2199,
        'fatalities': 260,
        'extreme_weather_days': 65,
        'disaster_breakdown': {
            'Cloudburst': 700,
            'Landslide': 1034, 
            'Floods': 300,
            'Drought': 100,
            'Others': 65
        }
    }

@anvil.server.callable
def get_impact_statistics():
    """Get organization impact statistics"""
    return {
        'farmers_empowered': 5000,
        'organic_villages': 120,
        'cottage_industries': 15,
        'solar_capacity': 8
    }