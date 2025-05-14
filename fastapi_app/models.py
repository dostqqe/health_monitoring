from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Date, Text, Time, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from fastapi_app.database import Base


class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    age = Column(Integer)
    sex = Column(Text)
    created_at = Column(Date, default=date.today)

    def __str__(self):
        return self.name

    contact_rules = relationship("PatientContactRule", back_populates="patient")
    disorders = relationship("PatientDisorder", back_populates="patient")
    metric_schedules = relationship("PatientMetricSchedule", back_populates="patient")
    indicators = relationship("HealthIndicator", back_populates="patient")
    cda_documents = relationship("CDADocument", back_populates="patient")
    voice_inputs = relationship("VoiceInput", back_populates="patient")
    monitoring_plans = relationship("MonitoringPlanPatient", back_populates="patient")
    dispensary_observations = relationship("DispensaryObservation", back_populates="patient")


class PatientContactRule(Base):
    __tablename__ = 'patient_contact_rules'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    rule_type = Column(Text)
    note = Column(Text)

    patient = relationship("Patient", back_populates="contact_rules")


class DispensaryObservation(Base):
    __tablename__ = 'dispensary_observation'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    disorder_id = Column(Integer, ForeignKey('disorders.id'))
    start_date = Column(Date)
    end_date = Column(Date)
    note = Column(Text)

    patient = relationship("Patient", back_populates="dispensary_observations")
    disorder = relationship("Disorder", back_populates="observations")

    def __str__(self):
        return f"{self.patient_id} ({self.id})"


class Disorder(Base):
    __tablename__ = 'disorders'
    id = Column(Integer, primary_key=True)
    mkd_code = Column(Text, unique=True)
    name = Column(Text)
    diagnosis_role = Column(Text)
    description = Column(Text)

    def __str__(self):
        return self.name

    patients = relationship("PatientDisorder", back_populates="disorder")
    observations = relationship("DispensaryObservation", back_populates="disorder")
    metric_reference_values = relationship("MetricReferenceValue", back_populates="disorder")
    metric_observations = relationship("DisorderMetricObservation", back_populates="disorder")
    metric_rules = relationship("DisorderMetricRule", back_populates="disorder")


class PatientDisorder(Base):
    __tablename__ = 'patient_disorders'
    patient_id = Column(Integer, ForeignKey('patients.id'), primary_key=True)
    disorder_id = Column(Integer, ForeignKey('disorders.id'), primary_key=True)

    patient = relationship("Patient", back_populates="disorders")
    disorder = relationship("Disorder", back_populates="patients")


class PatientMetricSchedule(Base):
    __tablename__ = 'patient_metric_schedule'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    metric_type_id = Column(Integer, ForeignKey('metric_type.id'))
    frequency = Column(Text)
    interval_days = Column(Text)
    time_of_day = Column(Time)
    start_day = Column(Date)
    end_day = Column(Date)
    description = Column(Text)

    patient = relationship("Patient", back_populates="metric_schedules")
    metric_type = relationship("MetricType", back_populates="schedules")


class HealthIndicator(Base):
    __tablename__ = 'health_indicators'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    day = Column(Date)
    result = Column(Text)
    metric_type_id = Column(Integer, ForeignKey('metric_type.id'))
    status = Column(Text)
    next_action = Column(Text)
    bot_transcript = Column(Text)
    source_type = Column(Text)
    is_valid = Column(Boolean)
    expires_at = Column(Date)

    patient = relationship("Patient", back_populates="indicators")
    metric_type = relationship("MetricType", back_populates="indicators")


class StorageSettings(Base):
    __tablename__ = 'storage_settings'
    id = Column(Integer, primary_key=True)
    text_response_retention_days = Column(Integer)


class MetricType(Base):
    __tablename__ = 'metric_type'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    external_code = Column(Text)
    external_system = Column(Text)

    def __str__(self):
        return self.name

    schedules = relationship("PatientMetricSchedule", back_populates="metric_type")
    indicators = relationship("HealthIndicator", back_populates="metric_type")
    reference_values = relationship("MetricReferenceValue", back_populates="metric_type")
    cda_metrics = relationship("CDADocumentMetric", back_populates="metric_type")
    observations = relationship("DisorderMetricObservation", back_populates="metric_type")
    plan_metrics = relationship("MonitoringPlanMetric", back_populates="metric_type")
    metric_rules = relationship("DisorderMetricRule", back_populates="metric_type")


class MetricReferenceValue(Base):
    __tablename__ = 'metric_reference_values'
    id = Column(Integer, primary_key=True)
    metric_type_id = Column(Integer, ForeignKey('metric_type.id'))
    min_value = Column(Integer)
    max_value = Column(Integer)
    sex = Column(Text)
    age_max = Column(Integer)
    age_min = Column(Integer)
    disorder_id = Column(Integer, ForeignKey('disorders.id'))
    reference_sours_id = Column(Integer, ForeignKey('reference_sources.id'))

    metric_type = relationship("MetricType", back_populates="reference_values")
    disorder = relationship("Disorder", back_populates="metric_reference_values")
    reference_source = relationship("ReferenceSource", back_populates="reference_values")


class CDADocument(Base):
    __tablename__ = 'cda_documents'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    document_xml = Column(Text)
    created_at = Column(Date)

    patient = relationship("Patient", back_populates="cda_documents")
    metrics = relationship("CDADocumentMetric", back_populates="cda_document")
    sources = relationship("ReferenceSource", back_populates="document")

    def __str__(self):
        return self.document_xml


class CDADocumentMetric(Base):
    __tablename__ = 'cda_document_metrics'
    id = Column(Integer, primary_key=True)
    cda_document_id = Column(Integer, ForeignKey('cda_documents.id'))
    metric_type_id = Column(Integer, ForeignKey('metric_type.id'))

    cda_document = relationship("CDADocument", back_populates="metrics")
    metric_type = relationship("MetricType", back_populates="cda_metrics")


class ReferenceSource(Base):
    __tablename__ = 'reference_sources'
    id = Column(Integer, primary_key=True)
    source_ref_id = Column(Integer, ForeignKey('cda_documents.id'))
    description = Column(Text)
    source_type = Column(Text)

    def __str__(self):
        return self.source_type

    document = relationship("CDADocument", back_populates="sources")
    reference_values = relationship("MetricReferenceValue", back_populates="reference_source")


class DisorderMetricObservation(Base):
    __tablename__ = 'disorder_metric_observation'
    id = Column(Integer, primary_key=True)
    disorder_id = Column(Integer, ForeignKey('disorders.id'))
    metric_type_id = Column(Integer, ForeignKey('metric_type.id'))
    priority = Column(Text)
    description = Column(Text)

    disorder = relationship("Disorder", back_populates="metric_observations")
    metric_type = relationship("MetricType", back_populates="observations")


class MonitoringPlan(Base):
    __tablename__ = 'monitoring_plan'
    id = Column(Integer, primary_key=True)
    created_by = Column(Integer, ForeignKey('users.id'))
    created_at = Column(Date)
    name = Column(Text)
    note = Column(Text)

    def __str__(self):
        return self.name

    creator = relationship("User", back_populates="monitoring_plans")
    patients = relationship("MonitoringPlanPatient", back_populates="plan")
    metrics = relationship("MonitoringPlanMetric", back_populates="plan")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    def __str__(self):
        return self.name

    monitoring_plans = relationship("MonitoringPlan", back_populates="creator")


class MonitoringPlanPatient(Base):
    __tablename__ = 'monitoring_plan_patients'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    plan_id = Column(Integer, ForeignKey('monitoring_plan.id'))

    patient = relationship("Patient", back_populates="monitoring_plans")
    plan = relationship("MonitoringPlan", back_populates="patients")


class MonitoringPlanMetric(Base):
    __tablename__ = 'monitoring_plan_metrics'
    id = Column(Integer, primary_key=True)
    plan_id = Column(Integer, ForeignKey('monitoring_plan.id'))
    metric_type_id = Column(Integer, ForeignKey('metric_type.id'))
    frequency = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)

    plan = relationship("MonitoringPlan", back_populates="metrics")
    metric_type = relationship("MetricType", back_populates="plan_metrics")


class VoiceInput(Base):
    __tablename__ = 'voice_inputs'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    text_response = Column(Text)
    recognized_metrics = Column(Text)
    recorded_at = Column(Date)
    note = Column(Text)

    patient = relationship("Patient", back_populates="voice_inputs")


class DisorderMetricRule(Base):
    __tablename__ = 'disorder_metric_rules'
    id = Column(Integer, primary_key=True)
    disorder_code = Column(Text, ForeignKey('disorders.mkd_code'))
    metric_type_id = Column(Integer, ForeignKey('metric_type.id'))
    note = Column(Text)

    disorder = relationship("Disorder", back_populates="metric_rules")
    metric_type = relationship("MetricType", back_populates="metric_rules")
