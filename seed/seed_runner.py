import csv
from sqlmodel import Session, select
 
from app.database import engine
from models.city import City, CityMetric
 
 
def run_seed():
    with Session(engine) as session:
        with open("app/seed/cities_seed.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
 
            for row in reader:
                # Check if city already exists
                stmt = select(City).where(City.name == row["name"])
                city = session.exec(stmt).first()
 
                if not city:
                    city = City(
                        name=row["name"],
                        state=row["state"],
                        population=int(row["population"]),
                    )
                    session.add(city)
                    session.commit()
                    session.refresh(city)
 
                # Add city metrics
                metric = CityMetric(
                    city_id=city.id,
                    year=int(row["year"]),
                    cost_of_living_index=float(row["cost_index"]),
                    air_quality_index=float(row["air_index"]),
                    safety_score=float(row["safety_score"]),
                    healthcare_score=float(row["health_score"]),
                )
 
                session.add(metric)
 
            session.commit()
 
    print("Seed complete!")
 
 
if __name__ == "__main__":
    run_seed()
 