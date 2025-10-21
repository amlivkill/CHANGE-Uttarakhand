from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
import datetime

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        self.setup_navigation()
        self.setup_hero_section()
        self.setup_contact_form()
        self.load_impact_stats()
    
    def setup_navigation(self):
        """Setup navigation button events"""
        # Navigation buttons
        self.btn_home.set_event_handler('click', self.show_home)
        self.btn_about.set_event_handler('click', self.show_about)
        self.btn_programs.set_event_handler('click', self.show_programs)
        self.btn_ai.set_event_handler('click', self.show_ai_tools)
        self.btn_climate.set_event_handler('click', self.show_climate)
        self.btn_products.set_event_handler('click', self.show_products)
        self.btn_contact.set_event_handler('click', self.show_contact)
        self.btn_submit.set_event_handler('click', self.submit_contact_form)
        
        # AI Tools buttons
        self.btn_crop_recommend.set_event_handler('click', self.get_crop_recommendation)
        self.btn_water_calc.set_event_handler('click', self.calculate_water_usage)
        self.btn_carbon_calc.set_event_handler('click', self.calculate_carbon_credits)
    
    def setup_hero_section(self):
        """Setup hero section content"""
        self.lbl_main_title.text = "🌿 CHANGE Uttarakhand"
        self.lbl_tagline.text = "Centre for Himalaya Agriculture and Nature Group of Environment"
        self.lbl_hero_title.text = "Transforming Rural Uttarakhand"
        self.lbl_hero_subtitle.text = "Sustainable Agriculture • Environmental Stewardship • Community Empowerment"
    
    def setup_contact_form(self):
        """Setup contact form dropdown"""
        self.dd_interest.items = [
            "Select your interest",
            "Membership", 
            "Volunteering",
            "Partnership",
            "Product Information", 
            "AI Consultation",
            "Training Programs",
            "Other"
        ]
        self.dd_interest.selected_value = "Select your interest"
    
    def load_impact_stats(self):
        """Load impact statistics from server"""
        try:
            stats = anvil.server.call('get_impact_statistics')
            self.lbl_farmers.text = f"{stats['farmers_empowered']}+"
            self.lbl_villages.text = f"{stats['organic_villages']}+"
            self.lbl_industries.text = f"{stats['cottage_industries']}"
            self.lbl_solar.text = f"{stats['solar_capacity']} MW"
        except Exception as e:
            print(f"Error loading stats: {e}")
    
    def show_home(self, **event_args):
        """Show home section"""
        self.column_panel_home.visible = True
        self.column_panel_about.visible = False
        self.column_panel_programs.visible = False
        self.column_panel_ai.visible = False
        self.column_panel_climate.visible = False
        self.column_panel_products.visible = False
        self.column_panel_contact.visible = False
    
    def show_about(self, **event_args):
        """Show about section"""
        self.column_panel_home.visible = False
        self.column_panel_about.visible = True
        self.column_panel_programs.visible = False
        self.column_panel_ai.visible = False
        self.column_panel_climate.visible = False
        self.column_panel_products.visible = False
        self.column_panel_contact.visible = False
    
    def show_programs(self, **event_args):
        """Show programs section"""
        self.column_panel_home.visible = False
        self.column_panel_about.visible = False
        self.column_panel_programs.visible = True
        self.column_panel_ai.visible = False
        self.column_panel_climate.visible = False
        self.column_panel_products.visible = False
        self.column_panel_contact.visible = False
    
    def show_ai_tools(self, **event_args):
        """Show AI tools section"""
        self.column_panel_home.visible = False
        self.column_panel_about.visible = False
        self.column_panel_programs.visible = False
        self.column_panel_ai.visible = True
        self.column_panel_climate.visible = False
        self.column_panel_products.visible = False
        self.column_panel_contact.visible = False
    
    def show_climate(self, **event_args):
        """Show climate section"""
        self.column_panel_home.visible = False
        self.column_panel_about.visible = False
        self.column_panel_programs.visible = False
        self.column_panel_ai.visible = False
        self.column_panel_climate.visible = True
        self.column_panel_products.visible = False
        self.column_panel_contact.visible = False
    
    def show_products(self, **event_args):
        """Show products section"""
        self.column_panel_home.visible = False
        self.column_panel_about.visible = False
        self.column_panel_programs.visible = False
        self.column_panel_ai.visible = False
        self.column_panel_climate.visible = False
        self.column_panel_products.visible = True
        self.column_panel_contact.visible = False
    
    def show_contact(self, **event_args):
        """Show contact section"""
        self.column_panel_home.visible = False
        self.column_panel_about.visible = False
        self.column_panel_programs.visible = False
        self.column_panel_ai.visible = False
        self.column_panel_climate.visible = False
        self.column_panel_products.visible = False
        self.column_panel_contact.visible = True

    # AI Tools Functions
    def get_crop_recommendation(self, **event_args):
        """Get AI crop recommendations"""
        soil_type = self.dd_soil_type.selected_value
        rainfall = self.dd_rainfall.selected_value
        altitude = self.dd_altitude.selected_value
        season = self.dd_season.selected_value
        
        if not all([soil_type, rainfall, altitude, season]):
            alert("Please select all parameters")
            return
        
        try:
            result = anvil.server.call('get_crop_recommendation', 
                                     soil_type, rainfall, altitude, season)
            self.lbl_crop_result.text = f"""
            🤖 AI Recommended Crops:
            
            Primary Crops:
            • {result['primary_crops'][0]}
            • {result['primary_crops'][1]} 
            • {result['primary_crops'][2]}
            
            Advisory:
            {result['advisory']}
            """
            
            # Log the query
            anvil.server.call('log_ai_query', 'crop_recommendation', 
                            f"Soil: {soil_type}, Rain: {rainfall}, Alt: {altitude}, Season: {season}",
                            "Success")
                            
        except Exception as e:
            alert(f"Error: {str(e)}")
            anvil.server.call('log_ai_query', 'crop_recommendation', 
                            f"Soil: {soil_type}, Rain: {rainfall}, Alt: {altitude}, Season: {season}",
                            f"Error: {str(e)}")
    
    def calculate_water_usage(self, **event_args):
        """Calculate water optimization"""
        try:
            crop_area = float(self.tb_crop_area.text) if self.tb_crop_area.text else 0
            crop_type = self.dd_crop_type.selected_value
            irrigation_type = self.dd_irrigation_type.selected_value
            
            if crop_area <= 0:
                alert("Please enter valid crop area")
                return
            
            result = anvil.server.call('calculate_water_usage', 
                                     crop_area, crop_type, irrigation_type)
            
            self.lbl_water_result.text = f"""
            💧 Water Optimization Results:
            
            Current Usage: {result['current_usage']:,.0f} liters/day
            Potential Savings: {result['savings']:,.0f} liters/day  
            System Efficiency: {result['efficiency']}
            """
            
            # Log the query
            anvil.server.call('log_ai_query', 'water_calculation',
                            f"Area: {crop_area}, Crop: {crop_type}, Irrigation: {irrigation_type}",
                            "Success")
                            
        except ValueError:
            alert("Please enter valid crop area")
        except Exception as e:
            alert(f"Error: {str(e)}")
            anvil.server.call('log_ai_query', 'water_calculation',
                            f"Area: {self.tb_crop_area.text}, Crop: {crop_type}, Irrigation: {irrigation_type}",
                            f"Error: {str(e)}")
    
    def calculate_carbon_credits(self, **event_args):
        """Calculate carbon credit income"""
        try:
            land_area = float(self.tb_land_area.text) if self.tb_land_area.text else 0
            farming_practice = self.dd_farming_practice.selected_value
            trees_planted = int(self.tb_trees_planted.text) if self.tb_trees_planted.text else 0
            practice_years = int(self.tb_practice_years.text) if self.tb_practice_years.text else 0
            
            if land_area <= 0:
                alert("Please enter valid land area")
                return
            
            result = anvil.server.call('calculate_carbon_credits',
                                     land_area, farming_practice, trees_planted, practice_years)
            
            self.lbl_carbon_result.text = f"""
            💰 Carbon Credit Analysis:
            
            Carbon Credits: {result['total_credits']:.1f} tCO2e
            Annual Income: ${result['income']:,.0f}
            Credit Value: ${result['credit_value']}/credit
            """
            
            # Log the query
            anvil.server.call('log_ai_query', 'carbon_calculation',
                            f"Land: {land_area}, Practice: {farming_practice}, Trees: {trees_planted}, Years: {practice_years}",
                            "Success")
                            
        except ValueError:
            alert("Please enter valid numbers")
        except Exception as e:
            alert(f"Error: {str(e)}")
            anvil.server.call('log_ai_query', 'carbon_calculation',
                            f"Land: {self.tb_land_area.text}, Practice: {farming_practice}, Trees: {self.tb_trees_planted.text}, Years: {self.tb_practice_years.text}",
                            f"Error: {str(e)}")
    
    def submit_contact_form(self, **event_args):
        """Submit contact form"""
        name = self.tb_name.text.strip()
        email = self.tb_email.text.strip()
        phone = self.tb_phone.text.strip()
        interest = self.dd_interest.selected_value
        message = self.ta_message.text.strip()
        
        # Validation
        if not name:
            alert("Please enter your name")
            return
        if not email:
            alert("Please enter your email")
            return
        if not message:
            alert("Please enter your message")
            return
        if interest == "Select your interest":
            alert("Please select your interest area")
            return
        
        try:
            success = anvil.server.call('save_contact_form', 
                                      name, email, phone, interest, message)
            if success:
                alert("""
                ✅ Thank you for your message!
                
                We have received your inquiry and our team 
                will get back to you within 24 hours.
                """)
                self.clear_contact_form()
            else:
                alert("There was an error submitting your form. Please try again.")
        except Exception as e:
            alert(f"Error: {str(e)}")
    
    def clear_contact_form(self):
        """Clear contact form fields"""
        self.tb_name.text = ""
        self.tb_email.text = "" 
        self.tb_phone.text = ""
        self.dd_interest.selected_value = "Select your interest"
        self.ta_message.text = ""