from fastapi import FastAPI, Request, Depends
from fastapi_app.admin_panel import PatientAdmin, setup_admin
from fastapi_app.routers import patient, disorder, health_indicator, metric_type, metric_reference_values
from fastapi_app.routers import patient_disorder, patient_contact_rules, dispensary_observation
from fastapi_app.routers import patient_metric_schedule, storage_settings
from fastapi_app.routers import cda_document, user, voice_input, disorder_metric_rules
from fastapi_app.routers import monitoring_plan, reference_sources, disorder_metric_observation, cda_document_metric
from fastapi_app.routers import monitoring_plan_patients, monitoring_plan_metrics
from sqladmin import Admin, ModelView
from fastapi_app.models import Patient
from fastapi_app.database import engine
app = FastAPI()
setup_admin(app)
@app.get("/")
def read_root():
    return {"message": "API is working"}

app.include_router(patient.router, prefix="/patients", tags=["Patients"])
app.include_router(disorder.router, prefix="/disorders", tags=["Disorders"])
app.include_router(health_indicator.router, prefix="/health_indicators", tags=["Health Indicator"])
app.include_router(metric_type.router, prefix="/metric_types", tags=["Metric Types"])
app.include_router(metric_reference_values.router, prefix="/metric_reference_values", tags=["Metric Reference Values"])
app.include_router(patient_disorder.router, prefix="/patient_disorders", tags=["Patient Disorders"])
app.include_router(patient_contact_rules.router, prefix="/contact_rules", tags=["ContactRules"])
app.include_router(dispensary_observation.router, prefix="/dispensary_observations", tags=["Dispensary Observations"])
app.include_router(patient_metric_schedule.router, prefix="/patient_metric_schedule", tags=["Patient Metric Schedule"])
app.include_router(storage_settings.router, prefix="/storage_settings", tags=["Storage Settings"])
app.include_router(cda_document.router, prefix="/cda_documents", tags=["CDA Documents"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(voice_input.router, prefix="/voice_inputs", tags=["Voice Inputs"])
app.include_router(disorder_metric_rules.router, prefix="/disorder_metric_rules", tags=["Disorder Metric Rules"])
app.include_router(monitoring_plan.router, prefix="/monitoring_plans", tags=["Monitoring Plan"])
app.include_router(reference_sources.router, prefix="/reference_sources", tags=["reference_sources"])
app.include_router(disorder_metric_observation.router, prefix="/disorder_metric_observations", tags=["disorder_metric_observations"])
app.include_router(cda_document_metric.router, prefix="/cda_document_metrics", tags=["CDADocumentMetrics"])
app.include_router(monitoring_plan_patients.router, prefix="/monitoring_plan_patients", tags=["Monitoring Patients"])
app.include_router(monitoring_plan_metrics.router, prefix="/monitoring_plan_metrics", tags=["Monitoring Patients"])

