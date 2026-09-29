import uuid
from sqlalchemy import Column, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class BudgetPlanModel(Base):
    __tablename__ = "budget_plans"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    total_budget = Column(Float, nullable=False)
    currency = Column(String, default="USD")
    preferences = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    items = relationship("PlanItemModel", back_populates="plan", cascade="all, delete-orphan")

class PlanItemModel(Base):
    __tablename__ = "plan_items"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    plan_id = Column(String, ForeignKey("budget_plans.id"))
    category_group = Column(String, nullable=False)
    item_name = Column(String, nullable=False)
    estimated_cost = Column(Float, nullable=False)
    priority = Column(String, default="Medium")
    notes = Column(Text, nullable=True)
    buying_tip = Column(Text, nullable=True)

    plan = relationship("BudgetPlanModel", back_populates="items")