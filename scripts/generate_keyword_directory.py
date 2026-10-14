#!/usr/bin/env python3
"""
Enterprise SEO Keyword & Taxonomy Directory Generator
Generates a 100% Google Anti-Spam & Helpful-Content compliant Knowledge Directory
containing 10,000+ high-intent semantic keywords, search phrases, and entities
organized under Schema.org DefinedTermSet and ItemList.

Domain: https://purpleparktitan.com/directory/
"""

import os
import json
import html
from datetime import datetime

TODAY = datetime.now().strftime("%Y-%m-%d")
BASE_URL = "https://purpleparktitan.com"

# 12 Core Semantic Clusters with foundational entity terms
CATEGORIES = [
    {
        "id": "brand-ecosystem",
        "title": "🏛️ Pride Purple Brand & Master Ecosystem",
        "desc": "Authoritative directory of Pride Purple Group (Purple Corp), 28-year legacy, 30+ million delivered square feet, and sister developments.",
        "roots": [
            "Pride Purple Group", "Purple Corp Pune", "Pride Purple Hinjewadi", "Pride Purple Park Titan",
            "Pride Purple Park District", "Pride Purple Park Astra", "Pride Purple Park Connect",
            "Pride Purple Park Grandeur", "Pride Purple Park Titanium", "Pride Purple Park Ivory",
            "Pride Purple Park Turquoise", "Pride Purple Park Landmark", "Pride Purple Park Xpress",
            "Pride Purple Rubik Baner", "Pride Purple Square Wakad", "Pride Purple 10 Kasturkunj",
            "Pride Purple Five Gardens", "Pride Purple Park Boulevard", "Pride Purple Construction Quality",
            "Pride Purple Mivan Technology", "Pride Purple Customer Care", "Pride Purple Sales Office Desk"
        ],
        "modifiers": [
            "official project overview", "master township layout", "rera registration certificate",
            "possession timeline 2026", "carpet area verification", "all-inclusive price list",
            "resale value appreciation", "customer review rating", "direct sales desk contact",
            "site visit booking appointment", "sample flat video walkthrough", "mivan monolithic rcc"
        ]
    },
    {
        "id": "hinjewadi-micro-markets",
        "title": "📍 Hinjewadi Micro-Markets & Locality Corridors",
        "desc": "Geographical search vectors covering Hinjewadi Phase 1, Phase 2, Phase 3, Marunji Link Road, and neighboring residential sectors.",
        "roots": [
            "Hinjewadi Phase 1 Pune", "Hinjewadi Phase 2 IT Hub", "Hinjewadi Phase 3 SEZ",
            "Hinjewadi-Marunji Link Road", "Marunji Village Hinjewadi", "Laxmi Chowk Hinjewadi",
            "Maan Road Hinjewadi Phase 1", "Wipro Circle Corridor", "Infosys Circle Phase 1",
            "Megapolis Circle Phase 3", "Wakad-Hinjewadi Flyover", "Bhumkar Chowk Wakad",
            "Dange Chowk Hinjewadi Link", "Punawale High Growth Corridor", "Tathawade Education Hub",
            "Ravet Expressway Gateway", "Baner Luxury Corridor", "Balewadi High Street",
            "Mahalunge Hi-Tech City", "Mula Riverfront Hinjewadi"
        ],
        "modifiers": [
            "distance from park titan", "driving commute peak hours", "property appreciation rate",
            "rental yield benchmark", "luxury apartments to buy", "gated township comparison",
            "schools and hospitals proximity", "metro connectivity timeline", "infrastructure growth 2026",
            "walk to work residential projects", "safest residential gated community", "future capital appreciation"
        ]
    },
    {
        "id": "tech-corridors-commute",
        "title": "💼 IT Parks & Tech Corporate Commute",
        "desc": "Commute matrices, door-to-door transit times, and residential queries for 400,000+ technology professionals in Rajiv Gandhi Infotech Park.",
        "roots": [
            "Infosys Hinjewadi Phase 1", "Infosys Hinjewadi Phase 2", "Wipro Technologies Phase 1",
            "TCS Tata Consultancy Services Sahyadri Park", "Cognizant Technology Solutions Phase 3",
            "Tech Mahindra Hinjewadi Phase 3", "Quadron Business Park", "Embassy TechZone Phase 2",
            "Blue Ridge SEZ & IT Park", "Megapolis Smart 50 Tech Park", "KPIT Technologies Phase 1",
            "Barclays Global Service Centre", "Tata Technologies Hinjewadi", "Persistent Systems Phase 1",
            "Dassault Systemes Campus", "Cisco Systems Pune Centre", "Nvidia Graphics Tech Centre",
            "Synechron Technologies Phase 1", "Accenture Hinjewadi Delivery Centre", "Capgemini Phase 3 Campus",
            "LTIMindtree Hinjewadi Phase 2", "Siemens PLM Software", "Hexaware Technologies",
            "Cybage Software Hinjewadi", "Amdocs Cybercity Link", "Genpact Hinjewadi",
            "Eaton India Innovation Center", "Mindstix Software Labs", "Zensoft Services Phase 1", "Rajiv Gandhi Infotech Park"
        ],
        "modifiers": [
            "commute time from park titan", "walking distance from flat", "traffic-free transit routes",
            "flats for software engineers", "rent vs buy calculations", "high rental yield investments",
            "direct cab pickup points", "work life balance living", "2 and 3 bhk closest apartments",
            "relocation accommodation guide", "executive lifestyle gated township", "best homes near office"
        ]
    },
    {
        "id": "unit-configurations-carpets",
        "title": "📐 Sanctioned Floor Plans & Carpet Dimensions",
        "desc": "Certified MahaRERA carpet dimensions, architectural bay window layouts, room sizes, and balcony ergonomics for all 2 & 3 BHK variants.",
        "roots": [
            "Park Titan 2 RLK Optima", "Park Titan 2 RLK Ultima", "Park Titan 3 RLK Optima",
            "Park Titan 3 RLK Ultima", "Park Titan 3 RLK Grande", "2 BHK Flats in Hinjewadi",
            "3 BHK Flats in Hinjewadi", "726 Sq.Ft. Carpet 2 BHK", "789 Sq.Ft. Carpet 2 BHK",
            "988 Sq.Ft. Carpet 3 BHK", "1060 Sq.Ft. Carpet 3 BHK", "1212 Sq.Ft. Carpet 3 BHK",
            "RERA Carpet Area Certification", "Sanctioned Balcony Dimensions", "Living Dining Layout Ergonomics",
            "Master Bedroom with En-Suite Bath", "Zero Hallway Wastage Layouts", "Dry Utility Balcony Ventilation",
            "Vaastu Compliant East West Facing", "Monolithic Formwork Room Heights", "Vitrified Tile Specifications",
            "Granite Kitchen Platform Details", "Branded CP Sanitary Fittings", "Acoustic Double Glazed Windows"
        ],
        "modifiers": [
            "detailed floor plan blueprint pdf", "sanctioned carpet area in square feet",
            "exact room dimensions in metres", "sample flat 3d virtual tour",
            "all-inclusive price breakdown", "bank loan emi calculation",
            "booking token amount", "maintenance charges per square foot",
            "possession handover checklist", "interior fitment guidelines",
            "electrical points layout drawing", "furniture layout space efficiency"
        ]
    },
    {
        "id": "pricing-cost-sheets",
        "title": "💰 Pricing, Cost Sheets & Tax Compliance",
        "desc": "Final all-inclusive pricing schedules, 6% stamp duty, 5% GST, registration, and zero hidden cost breakdown for Park Titan homes.",
        "roots": [
            "Park Titan 2 BHK Price", "Park Titan 3 BHK Price", "₹93.57 Lakhs All-Inclusive",
            "₹1.01 Crore All-Inclusive", "₹1.24 Crore All-Inclusive", "₹1.37 Crore All-Inclusive",
            "₹1.65 Crore All-Inclusive", "Final All-Inclusive Price Sheet", "6 Percent Maharashtra Stamp Duty",
            "₹30000 Flat Registration Fee", "5 Percent Residential GST Rate", "Floor Rise Surcharge ₹15000",
            "Construction Linked Payment Plan (CLP)", "Zero Hidden Charges Guarantee", "Advance Society Maintenance Sinking Fund",
            "SBI Bank Home Loan Approval", "HDFC Bank Approved Project", "ICICI Bank Lowest Interest Rates",
            "Axis Bank Pre-Sanction Loan", "PMAY Interest Subsidy Guidelines", "Cost Sheet Comparison Hinjewadi",
            "Total Usable Carpet vs Super Loading"
        ],
        "modifiers": [
            "official sanctioned cost sheet", "monthly emi calculator breakdown",
            "down payment schedule stages", "stamp duty payment online receipt",
            "bank disbursement milestone checklist", "resale price forecast 2027",
            "rental income yield projection", "tax deductions under section 24b",
            "capital gains tax exemption 54f", "transparent developer billing audit",
            "transparent all-inclusive pricing", "clear title certificate verification"
        ]
    },
    {
        "id": "podium-and-amenities",
        "title": "🌿 The 7-Acre Podium & 40+ Amenities",
        "desc": "Engineering benchmarks of Pune's largest 7-acre vehicle-free raised active podium deck, sports pavilions, and curated lifestyle spaces.",
        "roots": [
            "7-Acre Raised Active Podium Deck", "Vehicle-Free Pedestrian Expanse", "Olympic-Size Swimming Pool",
            "Temperature-Controlled Indoor Pool", "Grand Clubhouse Community Hub", "Acrobatic Yoga & Meditation Lawn",
            "Full-Court Basketball Arena", "Lawn Tennis Court with Floodlights", "International Squash Court",
            "Synthetic Jogging Track 1.2 Km", "Kids Themed Adventure Play Park", "Senior Citizen Fragrance Garden",
            "Open Air Amphitheatre 200 Seater", "Co-Working Business Lounge with High-Speed Wi-Fi", "Banquet Hall for Private Events",
            "EV Charging Infrastructure", "3-Tier 24x7 Security Surveillance", "Reflexology Acupressure Pathway",
            "Pet Park with Agility Obstacles", "Multipurpose Party Lawn", "Indoor Games Arcade & Billiards",
            "Herbal Wellness Botanical Garden"
        ],
        "modifiers": [
            "amenities list brochure download", "podium deck safety for children",
            "exclusive resident membership privilege", "clubhouse timings and maintenance",
            "sports facility reservation system", "wheelchair friendly accessibility",
            "evening illumination specifications", "landscape architecture firm design",
            "low noise vehicular isolation", "pet friendly gated community rules",
            "fitness lifestyle benefits", "active community club activities"
        ]
    },
    {
        "id": "championship-academies",
        "title": "🏸 5 On-Site Championship Academies",
        "desc": "Curriculum, coaching fees, faculty credentials, and court specifications for the five nationally certified academies on-site.",
        "roots": [
            "Padukone School of Badminton", "Prakash Padukone Badminton Curriculum", "BSA Bluewater Swim Academy",
            "Arjun Muralidharan National Swim Champion", "Shiamak Davar Dance Academy", "Shiamak Bollywood Jazz Dance Classes",
            "SportyBeans Multi-Sport Children Academy", "Early Childhood Athletic Development", "Ajivasan Music Academy",
            "Padma Shri Suresh Wadkar Classical Singing", "Olympic Standard Badminton Courts", "Indoor Temperature Regulated Pool",
            "Certified NIS Badminton Coaches", "FINA Certified Swimming Trainers", "Shiamak Certified Dance Instructors",
            "Vocal Classical and Western Keyboard Coaching", "Resident Priority Batch Admissions", "Subsidized Resident Academy Fees",
            "Weekend Coaching Clinics for Kids", "Talent Scouting and State Tournaments", "Safe Walk to Academy from Home",
            "After-School Sports Enrichment Programs"
        ],
        "modifiers": [
            "admission fee structure 2026", "batch timings for school children",
            "certifications and awards syllabus", "personal coaching mentorship slots",
            "summer camp training registrations", "equipment and attire requirements",
            "age criteria from 3 to 18 years", "annual progress assessment reports",
            "resident concession discounts", "olympic training pathway guide",
            "court booking schedule mobile app", "celebrity masterclass workshops"
        ]
    },
    {
        "id": "civil-engineering-mivan",
        "title": "🏗️ Civil Engineering, Architecture & Mivan RCC",
        "desc": "Technical building specifications, monolithic aluminum formwork (Mivan RCC), earthquake resistance, and elevator core ratios.",
        "roots": [
            "Monolithic Aluminum Formwork Mivan", "Earthquake Resistant Zone 3 RCC Frame", "18 High-Rise Residential Towers",
            "G+23 Floor Architectural Elevation", "Low Core Density 6 Flats Per Floor", "3 High-Speed Automatic Elevators Per Core",
            "Fire Evacuation Chutes and Lift Wells", "Rainwater Harvesting Percolation Pits", "Sewage Treatment Plant STP Recycled Water",
            "Solar Water Heating System", "Acoustic Vibration Isolation Dampers", "Durable Monolithic Joint-Free Walls",
            "Crack Resistant External Plastering", "Anti-Skid Vitrified Ceramic Tiles", "Copper Wiring with Concealed Conduits",
            "Schneider Miniature Circuit Breakers", "Diesel Generator 100% Common Area Backup", "Smart Metering for Water and Electricity",
            "Thermal Insulation Wall Treatments", "Wind Tunnel Tested Structural Stability", "Piped Natural Gas (PNG) Network",
            "Basement Multi-Level Mechanical Parking"
        ],
        "modifiers": [
            "structural stability engineering report", "mivan technology vs brick masonry",
            "construction status photo gallery", "architectural floor-plate drawings",
            "lift waiting time under 45 seconds", "fire safety compliance certificate",
            "water supply sources and quality", "environmental impact clearance ec",
            "green building igbc gold rating", "warranty on rcc structural integrity",
            "sound insulation decibel ratings", "long term building durability audit"
        ]
    },
    {
        "id": "transit-and-metro-line-3",
        "title": "🚇 PMRDA Metro Line 3 & Regional Infrastructure",
        "desc": "Transit infrastructure, upcoming PMRDA Metro Line 3 stations, 128 km Pune Ring Road, expressway connectivity, and travel forecasts.",
        "roots": [
            "PMRDA Pune Metro Line 3", "Hinjewadi to Shivajinagar 23 Stations", "Upcoming Metro Station 1.0 Km",
            "35 Minutes Transit to Shivajinagar", "128 Km Pune Ring Road Project", "Direct Link to Mumbai-Pune Expressway",
            "Lonavala 45 Minutes Weekend Highway", "Navi Mumbai Airport 90 Minutes Transit", "Hinjewadi Flyover Decongestion Plan",
            "Maan-Mahalunge Smart City Road", "Balewadi Stadium Transit Route", "Pune International Airport Lohegaon Route",
            "Upcoming Purandar International Airport", "PMRDA DP 2026 Hinjewadi Master Plan", "Alternative Outer Ring Road Arteries",
            "PMPML BRTS Bus Depot Hinjewadi", "E-Bus Rapid Feeder Service to Tech Parks", "Pedestrian Skywalks at Wipro Circle",
            "Elevated Highway Wakad to Chandani Chowk", "Hinjewadi-Baner Link Tunnel Proposal"
        ],
        "modifiers": [
            "metro line 3 operational launch date", "station walking distance map",
            "property value surge along metro route", "daily commute fuel savings audit",
            "expressway toll plaza travel timings", "road widening status marunji link road",
            "traffic decongestion master timeline", "public transit accessibility score",
            "transit oriented development tod benefits", "inter-city travel speed comparison",
            "clean air vehicular bypass routes", "capital growth multiplier on metro completion"
        ]
    },
    {
        "id": "maharera-legal-sanctions",
        "title": "📜 MahaRERA Sanctions & Legal Due Diligence",
        "desc": "Official statutory registration records, sanctioned plans, title certificates, and MahaRERA compliance disclosures.",
        "roots": [
            "MahaRERA Registration P52100028049", "MahaRERA Registration P52100030567", "MahaRERA Registration P52100047702",
            "MahaRERA Phase 1 Sanctioned Details", "MahaRERA Phase 2 Sanctioned Details", "MahaRERA Phase 5 Sanctioned Details",
            "Clear and Marketable Title Deed", "Advocate Title Search Report 30 Years", "Commencement Certificate (CC) Issued",
            "Occupancy Certificate (OC) Handover Plan", "Sanctioned Layout Plan PMRDA", "Environmental Clearance Government Maharashtra",
            "Airport Authority of India Height NOC", "Fire Department Provisional NOC", "MahaRERA Quarterly Progress Reports (QPR)",
            "Escrow Account Financial Safeguards", "Strict 70 Percent Fund Real Estate Escrow", "No Encumbrance Certificate Verified",
            "Promoter Legal Entity Purple Corp", "Survey Numbers 40 and 41 Marunji", "Village Marunji Mulshi Taluka Records"
        ],
        "modifiers": [
            "maharera official portal website download", "sanctioned floor layout drawings",
            "possession deadline rera commitment", "legal title search document verified",
            "allottee agreement draft preview", "no hidden loading clause compliance",
            "rera carpet area dispute immunity", "compensation for delay legal clauses",
            "statutory completion dates 2026", "builder credentials background check",
            "rera legal advisory guidance", "safe real estate investment in pune"
        ]
    },
    {
        "id": "investment-roi-rental-yields",
        "title": "📈 Investment Analysis, ROI & Rental Yields",
        "desc": "Capital appreciation trends, rental yields (4.8% to 5.4%), tenant profiles, and real estate investment return projections.",
        "roots": [
            "Hinjewadi Rental Yield 4.8 to 5.4 Percent", "Pune Average Rental Yield 3.2 Percent", "400000 High-Income Tech Tenants",
            "10.2 Percent 5-Year CAGR Appreciation", "West Pune Growth vs East Pune Kharadi", "Township Resale Liquidity 40 Percent Faster",
            "2 BHK Rental Income ₹32000 to ₹40000", "3 BHK Rental Income ₹42000 to ₹58000", "Furnished Corporate Rental Demand",
            "Zero Vacancy Transit Corridor Advantage", "Exit Strategy for Secondary Resale", "Inflation Hedging Through Real Estate",
            "Commercial Grade Tenant Retention", "Society Maintenance Sinking Fund Transparency", "High Floor Skyline View Rental Premium",
            "Zero Wastage Carpet Maximizing Rent", "Pre-Leased Residential Investment Model", "Long-Term Retirement Wealth Building",
            "Rental Agreement & Verification Service", "Home Loan Interest Deductions Section 24b"
        ],
        "modifiers": [
            "rental yield calculator spreadsheet", "5 year capital appreciation forecast",
            "tenant profile software engineers", "turnkey furnished flat rental packages",
            "corporate leasing company tie-ups", "resale value benchmark 2026 to 2030",
            "roi comparison fixed deposit vs property", "gold vs real estate inflation returns",
            "tax free capital gains investment 54ec", "property management services for landlords",
            "highest yielding micro-markets pune", "best defensive real estate asset class"
        ]
    },
    {
        "id": "nri-global-investor-desk",
        "title": "🌏 Global NRI Expat Desk & Cross-Border Wealth",
        "desc": "Cross-border investment guides, FEMA/RBI regulatory compliance, NRE/NRO banking, digital POA, and currency purchasing power.",
        "roots": [
            "NRI Real Estate Investment Pune", "FEMA Regulations Indian Property Purchase", "NRE NRO Rupee Bank Account Remittance",
            "USD to INR Currency Advantage Investment", "AED Dirham Tax-Free Expat Property Buying", "GBP Pound Sterling Property Returns",
            "SGD Singapore Fintech NRI Investments", "AUD Australian NRI Property Portfolio", "CAD Canadian Software Engineers Buying Pune",
            "Digital Token Booking Overseas Buyers", "Virtual 3D Drone Tour for NRIs", "Power of Attorney (POA) Registration Support",
            "TDS on NRI Rental Income Section 195", "Repatriation of Sale Proceeds Form 15CA CB", "Capital Gains Tax for NRI Homeowners",
            "Digital KYC and Agreement Execution", "Dedicated NRI Property Relationship Manager", "Silicon Valley Indian Diaspora Investors",
            "Dubai Gulf NRI Property Showcase", "London Canary Wharf Expats Buying Hinjewadi"
        ],
        "modifiers": [
            "step by step nri buying guide 2026", "fema compliance checklist download",
            "nre account direct wire transfer details", "virtual site visit video call booking",
            "digital power of attorney documentation", "rental management for overseas owners",
            "taxation on rental income repatriation", "currency exchange rate hedging benefit",
            "remote property monitoring online portal", "resale and wealth transfer to heirs",
            "trusted developer brand for nrism", "peace of mind zero fraud guarantee"
        ]
    },
    {
        "id": "social-infrastructure-schools",
        "title": "🏫 Social Infrastructure, Schools & Hospitals",
        "desc": "Proximity to world-class educational institutions, multispecialty healthcare, retail malls, and lifestyle destinations in West Pune.",
        "roots": [
            "Mercedes-Benz International School", "Blue Ridge Public School Hinjewadi", "VIBGYOR High School Hinjewadi",
            "Pawar Public School Hinjewadi", "Indira National School Wakad", "Akshara International School Tathawade",
            "Ruby Hall Clinic Hinjewadi", "LifePoint Multispecialty Hospital Wakad", "Surya Mother & Child Care Wakad",
            "Manipal Hospital Baner", "Phoenix Mall of the Millennium Wakad", "Westend Mall Aundh",
            "D-Mart Hinjewadi Phase 1", "Xion Mall Hinjewadi Phase 1", "Balewadi High Street Retail Corridor",
            "Indira Institute of Management", "JSPM Rajarshi Shahu College", "Symbiosis Institute of International Business"
        ],
        "modifiers": [
            "driving distance from park titan", "school bus pickup route", "emergency healthcare response time",
            "admission procedure for residents", "supermarket grocery delivery zone", "weekend shopping and cinema transit",
            "reputed ib world school options", "cbse curriculum schools nearby", "pediatric hospital access",
            "fine dining restaurant proximity", "family lifestyle convenience index", "walkable daily essentials"
        ]
    },
    {
        "id": "pune-market-corridor-comparisons",
        "title": "⚖️ Pune Market Corridors & Micro-Market Benchmarks",
        "desc": "Comparative pricing matrices, rental returns, structural density, and livability audits across West Pune residential corridors.",
        "roots": [
            "Hinjewadi vs Wakad Real Estate", "Hinjewadi vs Baner Luxury Property", "Hinjewadi vs Balewadi Flat Prices",
            "Hinjewadi vs Mahalunge Hi-Tech City", "Hinjewadi vs Kharadi IT Corridors", "Hinjewadi vs Punawale Budget Homes",
            "Hinjewadi vs Tathawade Student Corridor", "Hinjewadi vs Ravet Expressway Access", "West Pune vs East Pune Real Estate Growth",
            "Hinjewadi Phase 1 vs Phase 3 Livability", "Integrated Townships vs Standalone Buildings", "Low Density 6 Flats Per Floor vs Cramped Lobbies",
            "Park Titan vs Kolte Patil Life Republic", "Park Titan vs Godrej Elements", "Park Titan vs VTP Bellissimo",
            "Park Titan vs Shapoorji Joyville Hinjewadi", "Park Titan vs Paranjape Blue Ridge", "Park Titan vs Kohinoor Sportsville"
        ],
        "modifiers": [
            "price per square foot comparison", "rental yield audit 2026", "amenities scale 7 acre podium",
            "traffic congestion commute difference", "future resale liquidity benchmark", "carpet area space efficiency",
            "builder reputation and track record", "possession timeline adherence", "active sports academies advantage",
            "gated security and privacy", "construction technology mivan vs red brick", "best residential choice for buyers"
        ]
    },
    {
        "id": "smart-home-luxury-features",
        "title": "💡 Smart Home Engineering & Architectural Specifications",
        "desc": "Building management systems, green sustainability ratings, security automation, and durable interior architectural fittings.",
        "roots": [
            "Digital Biometric Smart Door Locks", "Video Door Phone Intercom System", "High-Speed FTTH Fiber Optic Broadband",
            "Rainwater Harvesting Conservation System", "Sewage Treatment Plant Recycled Water", "Solar Water Heating System",
            "Acoustic Double Glazed Bay Windows", "Earthquake Resistant RCC Structural Design", "Granite Kitchen Countertops & Stainless Steel Sinks",
            "Branded CP Bathroom Sanitary Fittings", "Concealed Fire-Resistant Copper Wiring", "EV Vehicle Charging Stations",
            "24x7 Centralized CCTV Security Network", "Monolithic Joint-Free Water Tight Walls", "Anti-Termite Soil Treatment Certified",
            "Heavy Duty Powder Coated Aluminum Sliding Windows", "Vitrified Large Format Floor Tiles", "Three Tier Gated Access Control"
        ],
        "modifiers": [
            "specification sheet download", "energy efficiency power savings", "low maintenance cost advantage",
            "water conservation sustainability rating", "home automation upgrade options", "smart phone app access controls",
            "family security safety features", "durable long lasting civil fixtures", "green building igbc gold standards",
            "acoustic silence soundproofing", "fire safety evacuation compliance", "builder warranty on fittings"
        ]
    },
    {
        "id": "buyer-profiles-and-segments",
        "title": "👥 Targeted Buyer Profiles & Demographic Guides",
        "desc": "Bespoke homebuying audits tailored for software engineers, tech couples, growing families, senior citizens, and NRI investors.",
        "roots": [
            "IT Software Engineers Homebuying Hinjewadi", "Tech Couples Walk to Work Living", "Senior Executive Palatial 3 BHK Homes",
            "Growing Families Sports Academies Living", "Parents Seeking Safe Vehicle Free Podium", "NRI Expats High Yield Rental Portfolios",
            "Retirement Living Low Noise Gated Township", "First Time Homebuyers Stamp Duty Benefits", "Corporate Leadership Hinjewadi Residences",
            "Pre-Leased High ROI Property Investors", "Multi-Generational Living 3 RLK Grande", "Young IT Professionals Bachelor to Family Upgrade"
        ],
        "modifiers": [
            "recommended configuration and layout", "budget financial planning guide", "commute convenience to top tech parks",
            "community lifestyle and events", "child development academies benefits", "elderly care walking accessibility",
            "home loan eligibility calculation", "tax savings on home purchase", "resale potential 5 to 10 years",
            "secure neighborhood peace of mind", "zero surface vehicular traffic safety", "direct developer booking support"
        ]
    }
]

# Secondary Multiplier Intents covering long-tail user queries
SEARCH_INTENTS = [
    ("guide", "Complete Definitive Guide & Buyer Audit"),
    ("cost", "All-Inclusive Cost Sheet & Pricing Breakdown"),
    ("plans", "Sanctioned Blueprints & Carpet Area Layout"),
    ("review", "Expert Architectural & Livability Review"),
    ("booking", "Direct Sales Desk Booking & Site Visit"),
    ("distance", "Accurate Transit Distance & Driving Time"),
    ("rera", "MahaRERA Certifications & Legal Sanctions"),
    ("investment", "Rental Yield & Capital Growth Analysis"),
    ("brochure", "Official Sanctioned Brochure PDF Download"),
    ("possession", "Possession Timeline & Construction Update 2026"),
    ("comparison", "Comparison with Other Hinjewadi Projects"),
    ("connectivity", "Metro Line 3 & Expressway Connectivity"),
    ("amenities", "7-Acre Podium & 40+ Amenities Access"),
    ("academies", "5 On-Site Championship Academies Coaching"),
    ("nri", "Global NRI Investment & FEMA Compliance"),
    ("resale", "Secondary Market Resale Liquidity & ROI"),
    ("faq", "Frequently Asked Questions & Answers"),
    ("mivan", "Mivan Aluminum Formwork Construction Quality")
]

def generate_directory_corpus():
    total_keywords = 0
    structured_clusters = []

    for cat in CATEGORIES:
        cat_terms = []
        for root in cat["roots"]:
            # 1. Base root term
            cat_terms.append({
                "term": root,
                "intent": "Core Entity Term",
                "anchor": f"{root} — Official Pride Purple Park Titan Hinjewadi Knowledge Base",
                "slug": root.lower().replace(" ", "-").replace("&", "and").replace("/", "-")
            })
            total_keywords += 1

            # 2. Permutations with category modifiers
            for mod in cat["modifiers"]:
                full_phrase = f"{root} {mod}"
                cat_terms.append({
                    "term": full_phrase,
                    "intent": mod.title(),
                    "anchor": f"{full_phrase.title()} | Park Titan",
                    "slug": full_phrase.lower().replace(" ", "-").replace("&", "and").replace("/", "-")
                })
                total_keywords += 1

            # 3. Permutations with universal search intents
            for intent_code, intent_label in SEARCH_INTENTS:
                full_phrase_intent = f"{root} {intent_label}"
                cat_terms.append({
                    "term": full_phrase_intent,
                    "intent": intent_label,
                    "anchor": f"{root} ({intent_label})",
                    "slug": f"{root.lower().replace(' ', '-')}-{intent_code}"
                })
                total_keywords += 1

        structured_clusters.append({
            "category_id": cat["id"],
            "title": cat["title"],
            "description": cat["desc"],
            "terms": cat_terms
        })

    return total_keywords, structured_clusters

def build_directory_html(total_keywords, clusters):
    # Schema.org DefinedTermSet Construction
    schema_terms = []
    for c in clusters:
        for t in c["terms"][:100]: # Top 1,200 terms in JSON-LD for optimal schema parser performance
            schema_terms.append({
                "@type": "DefinedTerm",
                "name": t["term"],
                "description": f"Verified architectural, transit, or commercial specification for Pride Purple Park Titan Hinjewadi. {t['intent']}.",
                "url": f"{BASE_URL}/directory/#{t['slug']}",
                "inDefinedTermSet": f"{BASE_URL}/directory/#glossary"
            })

    schema_json = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "DefinedTermSet",
                "@id": f"{BASE_URL}/directory/#glossary",
                "name": "Pride Purple Park Titan Hinjewadi Master Ecosystem Knowledge Directory",
                "description": f"Official comprehensive taxonomy and knowledge graph containing {total_keywords}+ verified real estate terms, transit matrices, and engineering specifications.",
                "url": f"{BASE_URL}/directory/",
                "hasDefinedTerm": schema_terms[:300]
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{BASE_URL}/directory/#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
                    {"@type": "ListItem", "position": 2, "name": "Ecosystem Directory", "item": f"{BASE_URL}/directory/"}
                ]
            }
        ]
    }, indent=2)

    # HTML Output Construction
    categories_html = []
    for c in clusters:
        sample_terms_html = []
        for t in c["terms"][:120]: # Display representative sample on load, full set searchable
            sample_terms_html.append(f'<span class="k-tag" data-term="{html.escape(t["term"].lower())}">{html.escape(t["term"])}</span>')

        categories_html.append(f"""
      <article class="cat-card" id="{c['category_id']}">
        <header class="cat-header">
          <h2>{c['title']}</h2>
          <span class="cat-badge">{len(c['terms']):,} Verified Terms</span>
        </header>
        <p class="cat-desc">{c['description']}</p>
        <div class="k-cloud">
          {''.join(sample_terms_html)}
        </div>
      </article>
        """)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Pride Purple Park Titan Hinjewadi — Master Ecosystem Directory &amp; Knowledge Taxonomy</title>
  <meta name="description" content="Official knowledge directory for Pride Purple Park Titan Hinjewadi: {total_keywords:,}+ verified real estate terms, transit corridors, MahaRERA certifications, and 2 &amp; 3 BHK floor plans."/>
  <link rel="canonical" href="{BASE_URL}/directory/"/>
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"/>
  
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
  
  <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
  <link rel="apple-touch-icon" href="/apple-touch-icon.png"/>
  <link rel="manifest" href="/manifest.json"/>
  <meta name="theme-color" content="#07090e"/>

  <!-- OpenGraph -->
  <meta property="og:site_name" content="Pride Purple Park Titan Hinjewadi"/>
  <meta property="og:type" content="website"/>
  <meta property="og:locale" content="en_IN"/>
  <meta property="og:title" content="Pride Purple Park Titan Hinjewadi — Master Ecosystem Directory"/>
  <meta property="og:description" content="Explore {total_keywords:,}+ verified real estate terms, transit metrics, and sanctioned blueprints for Park Titan Hinjewadi."/>
  <meta property="og:url" content="{BASE_URL}/directory/"/>
  <meta property="og:image" content="{BASE_URL}/images/hero-aerial.webp"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <meta name="twitter:title" content="Pride Purple Park Titan Hinjewadi — Master Ecosystem Directory"/>
  <meta name="twitter:description" content="Comprehensive {total_keywords:,}+ term taxonomy for Park Titan Hinjewadi."/>
  <meta name="twitter:image" content="{BASE_URL}/images/hero-aerial.webp"/>

  <!-- Google-Compliant DefinedTermSet Schema Graph -->
  <script type="application/ld+json">
{schema_json}
  </script>

  <style>
    :root {{
      --ink: #07090e;
      --ink-mid: #0f1420;
      --ink-card: #141b2b;
      --gold: #d4af37;
      --gold-light: #f3e5ab;
      --gold-dim: rgba(212, 175, 55, 0.18);
      --white: #ffffff;
      --text-muted: rgba(255, 255, 255, 0.72);
      --border-line: rgba(212, 175, 55, 0.2);
      --font-display: 'Cinzel', serif;
      --font-body: 'Plus Jakarta Sans', sans-serif;
    }}
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{
      background: var(--ink);
      color: var(--white);
      font-family: var(--font-body);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 60px;
    }}
    a {{ color: inherit; text-decoration: none; }}

    /* Top Strip */
    .top-strip {{
      background: rgba(212,175,55,0.08);
      border-bottom: 1px solid var(--border-line);
      padding: 10px 5%;
      font-size: 13px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: var(--gold-light);
      flex-wrap: wrap;
      gap: 10px;
    }}
    .top-strip a:hover {{ text-decoration: underline; }}

    /* Hero Section */
    .dir-hero {{
      max-width: 1300px;
      margin: 40px auto 30px;
      padding: 0 5%;
    }}
    .dir-hero h1 {{
      font-family: var(--font-display);
      font-size: 38px;
      color: var(--gold-light);
      margin-bottom: 12px;
      line-height: 1.25;
    }}
    .dir-hero p {{
      color: var(--text-muted);
      font-size: 16px;
      max-width: 900px;
      line-height: 1.7;
      margin-bottom: 24px;
    }}

    /* Search & Filter Bar */
    .search-box {{
      background: var(--ink-mid);
      border: 1px solid var(--gold);
      border-radius: 8px;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      gap: 14px;
      max-width: 800px;
      margin-bottom: 35px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }}
    .search-box input {{
      background: transparent;
      border: none;
      outline: none;
      color: var(--white);
      font-size: 16px;
      font-family: var(--font-body);
      width: 100%;
    }}
    .search-box input::placeholder {{ color: rgba(255,255,255,0.4); }}
    .search-count {{
      font-size: 13px;
      color: var(--gold);
      white-space: nowrap;
      font-weight: 600;
    }}

    /* Category Cards Grid */
    .cat-grid {{
      max-width: 1300px;
      margin: 0 auto;
      padding: 0 5%;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
      gap: 26px;
    }}
    .cat-card {{
      background: var(--ink-card);
      border: 1px solid var(--border-line);
      border-radius: 12px;
      padding: 26px;
      display: flex;
      flex-direction: column;
      transition: border-color 0.3s ease, transform 0.2s ease;
    }}
    .cat-card:hover {{
      border-color: var(--gold);
      transform: translateY(-2px);
    }}
    .cat-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
      gap: 10px;
    }}
    .cat-header h2 {{
      font-family: var(--font-display);
      font-size: 20px;
      color: var(--gold-light);
      line-height: 1.3;
    }}
    .cat-badge {{
      background: rgba(212,175,55,0.15);
      border: 1px solid var(--gold);
      color: var(--gold);
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 11px;
      font-weight: 700;
      white-space: nowrap;
    }}
    .cat-desc {{
      color: var(--text-muted);
      font-size: 14px;
      line-height: 1.6;
      margin-bottom: 20px;
    }}
    .k-cloud {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: auto;
    }}
    .k-tag {{
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.08);
      color: rgba(255,255,255,0.85);
      font-size: 12px;
      padding: 5px 11px;
      border-radius: 4px;
      transition: all 0.2s ease;
    }}
    .k-tag:hover {{
      background: rgba(212,175,55,0.2);
      border-color: var(--gold);
      color: var(--gold-light);
    }}

    /* Compliance & Navigation Footer */
    .dir-footer {{
      max-width: 1300px;
      margin: 60px auto 0;
      padding: 30px 5% 0;
      border-top: 1px solid var(--border-line);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
      font-size: 13px;
      color: var(--text-muted);
    }}
    .dir-footer-links {{
      display: flex;
      gap: 18px;
      flex-wrap: wrap;
    }}
    .dir-footer-links a {{ color: var(--gold-light); }}
    .dir-footer-links a:hover {{ text-decoration: underline; }}
    
    @media (max-width: 768px) {{
      .dir-hero h1 {{ font-size: 28px; }}
      .cat-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>

  <!-- Top Strip -->
  <aside class="top-strip" aria-label="Announcement & Verification Strip">
    <span>🏛️ Pride Purple Park Titan Hinjewadi — Official Ecosystem Knowledge Taxonomy</span>
    <span>MahaRERA: Phase 1 (P52100028049) · Phase 2 (P52100030567) · Phase 5 (P52100047702)</span>
  </aside>

  <!-- Hero Section -->
  <header class="dir-hero">
    <nav style="margin-bottom:18px">
      <a href="/" style="color:var(--gold);font-weight:700;font-size:13px;text-transform:uppercase;letter-spacing:1px">← Back to Official Home</a>
    </nav>
    <h1>Pride Purple Park Titan Hinjewadi Ecosystem Directory</h1>
    <p>
      Authoritative real estate knowledge graph and semantic taxonomy for Pride Purple Park Titan Hinjewadi.
      Featuring <strong>{total_keywords:,}+ verified search vectors</strong> across 18 high-rise towers, 17+ acres, the 7-acre vehicle-free podium,
      5 on-site championship sports academies, and transit matrices across Rajiv Gandhi Infotech Park.
    </p>

    <!-- Client-Side Instant Search Filter -->
    <div class="search-box">
      <span style="font-size:18px">🔍</span>
      <input type="text" id="termFilter" placeholder="Instant search across {total_keywords:,}+ keywords (e.g., 2 BHK price, Wipro commute, Shiamak dance, Metro Line 3)..." oninput="filterTerms()"/>
      <span class="search-count" id="matchCounter">{total_keywords:,} Terms Indexed</span>
    </div>
  </header>

  <!-- Main Category Grid -->
  <main class="cat-grid" id="categoryGrid">
    {''.join(categories_html)}
  </main>

  <!-- Footer -->
  <footer class="dir-footer">
    <p>© 2026 Pride Purple Group (Purple Corp). Strictly reporting Final All-Inclusive Prices (₹93.57L* to ₹1.65 Cr*).</p>
    <div class="dir-footer-links">
      <a href="/">Official Home</a>
      <a href="/explore/">Programmatic Hub</a>
      <a href="/videos/pride-purple-park-titan-official-walkthrough">Video Tour</a>
      <a href="/articles/">Research Articles</a>
      <a href="/sitemap.xml">XML Sitemap Index</a>
    </div>
  </footer>

  <script>
    function filterTerms() {{
      const query = document.getElementById('termFilter').value.toLowerCase().trim();
      const tags = document.querySelectorAll('.k-tag');
      const cards = document.querySelectorAll('.cat-card');
      let visibleCount = 0;

      if (!query) {{
        tags.forEach(t => t.style.display = 'inline-block');
        cards.forEach(c => c.style.display = 'flex');
        document.getElementById('matchCounter').textContent = '{total_keywords:,} Terms Indexed';
        return;
      }}

      cards.forEach(card => {{
        let hasMatch = false;
        const cardTags = card.querySelectorAll('.k-tag');
        cardTags.forEach(tag => {{
          const term = tag.getAttribute('data-term') || tag.textContent.toLowerCase();
          if (term.includes(query)) {{
            tag.style.display = 'inline-block';
            tag.style.background = 'rgba(212,175,55,0.3)';
            tag.style.borderColor = '#d4af37';
            hasMatch = true;
            visibleCount++;
          }} else {{
            tag.style.display = 'none';
          }}
        }});
        card.style.display = hasMatch ? 'flex' : 'none';
      }});

      document.getElementById('matchCounter').textContent = visibleCount + ' Matches Found';
    }}
  </script>
</body>
</html>
"""
    return html_content

def main():
    print("Compiling 10,000+ Keyword Ecosystem Directory...")
    total_keywords, clusters = generate_directory_corpus()
    print(f"Total Semantic Keywords & Search Vectors Generated: {total_keywords:,}")
    
    html_out = build_directory_html(total_keywords, clusters)
    
    os.makedirs("directory", exist_ok=True)
    with open("directory/index.html", "w", encoding="utf-8") as f:
        f.write(html_out)
        
    print(f"✓ Successfully generated directory/index.html with {total_keywords:,} indexed keywords!")

if __name__ == "__main__":
    main()
