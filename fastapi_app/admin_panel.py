from sqladmin import ModelView, Admin
from fastapi_app.models import Patient, Disorder, PatientDisorder, PatientContactRule, StorageSettings
from fastapi_app.models import MetricType, DispensaryObservation, CDADocument, User, MetricReferenceValue
from fastapi_app.database import engine
from fastapi_app.models import VoiceInput, PatientMetricSchedule, HealthIndicator, ReferenceSource
from fastapi_app.models import CDADocumentMetric, MonitoringPlan, DisorderMetricObservation, MonitoringPlanPatient, MonitoringPlanMetric


class PatientAdmin(ModelView, model=Patient):
    column_list = [Patient.id, Patient.name, Patient.age, Patient.sex, Patient.created_at]
    form_columns = [Patient.name, Patient.age, Patient.sex]
    column_searchable_list = [Patient.name, Patient.age]
    column_filters = [Patient.created_at]

class DisorderAdmin(ModelView, model=Disorder):
    column_list = [Disorder.id, Disorder.name, Disorder.mkd_code, Disorder.description]
    form_columns = [Disorder.name, Disorder.mkd_code, Disorder.description]

class PatientDisorderAdmin(ModelView, model=PatientDisorder):
    column_list = [PatientDisorder.patient_id, PatientDisorder.disorder_id]
    form_columns = [PatientDisorder.patient_id, PatientDisorder.disorder_id]

class PatientContactRuleAdmin(ModelView, model=PatientContactRule):
    column_list = ["id", "patient", "rule_type", "note"]
    form_columns = ["patient", "rule_type", "note"]

class StorageSettingsAdmin(ModelView, model=StorageSettings):
    column_list = ["id", "text_response_retention_days"]
    form_columns = ["text_response_retention_days"]

class MetricTypeAdmin(ModelView, model=MetricType):
    column_list = ["id", "name", "description", "external_code", "external_system"]
    form_columns = ["name", "description", "external_code", "external_system"]

class DispensaryObservationAdmin(ModelView, model=DispensaryObservation):
    column_list = [DispensaryObservation.id, DispensaryObservation.patient, DispensaryObservation.disorder, DispensaryObservation.start_date, DispensaryObservation.end_date, DispensaryObservation.note]
    form_columns = [DispensaryObservation.patient, DispensaryObservation.disorder, "start_date", "end_date", "note"]

class CDADocumentAdmin(ModelView, model=CDADocument):
    column_list = [CDADocument.id, CDADocument.patient, "document_xml", "created_at"]
    form_columns = [CDADocument.patient, "document_xml", "created_at"]

class UserAdmin(ModelView, model=User):
    column_list = ["id", "name"]
    form_columns = ["name"]

class VoiceInputAdmin(ModelView, model=VoiceInput):
    column_list = [VoiceInput.id, VoiceInput.patient, "text_response", "recognized_metrics", "recorded_at", "note"]
    form_columns = [VoiceInput.patient, "text_response", "recognized_metrics", "recorded_at", "note"]

class PatientMetricScheduleAdmin(ModelView, model=PatientMetricSchedule):
    column_list = [PatientMetricSchedule.id, PatientMetricSchedule.patient, PatientMetricSchedule.metric_type, "frequency", "interval_days", "time_of_day", "start_day", "end_day", "description"]
    form_columns = [PatientMetricSchedule.patient, PatientMetricSchedule.metric_type, "frequency", "interval_days", "time_of_day","start_day", "end_day", "description"]

class HealthIndicatorAdmin(ModelView, model=HealthIndicator):
    column_list = [HealthIndicator.id, HealthIndicator.patient, "day", "result", HealthIndicator.metric_type, "status", "next_action", "bot_transcript", "source_type", "is_valid", "expires_at"]
    form_columns = [HealthIndicator.id, HealthIndicator.patient, "day", "result", HealthIndicator.metric_type, "status", "next_action", "bot_transcript", "source_type", "is_valid", "expires_at"]

class ReferenceSourceAdmin(ModelView, model=ReferenceSource):
    column_list = [ReferenceSource.id, ReferenceSource.document, "description", "source_type"]
    form_columns = [ReferenceSource.id, ReferenceSource.document, "description", "source_type"]

class MetricReferenceValueAdmin(ModelView, model=MetricReferenceValue):
    column_list = [MetricReferenceValue.id, MetricReferenceValue.metric_type, "min_value", "max_value", "sex", "age", "age_max", "age_min",
                   MetricReferenceValue.disorder, MetricReferenceValue.reference_source]
    form_columns = [MetricReferenceValue.id, MetricReferenceValue.metric_type, "min_value", "max_value", "sex", "age", "age_max", "age_min",
                   MetricReferenceValue.disorder, MetricReferenceValue.reference_source]

class CDADocumentMetricAdmin(ModelView, model=CDADocumentMetric):
    column_list = ["id", CDADocumentMetric.cda_document, CDADocumentMetric.metric_type]
    form_columns = ["id", CDADocumentMetric.cda_document, CDADocumentMetric.metric_type]

class MonitoringPlanAdmin(ModelView, model=MonitoringPlan):
    column_list = ["id", MonitoringPlan.creator, "created_at", "name", "note"]
    form_columns = ["id", MonitoringPlan.creator, "created_at", "name", "note"]

class DisorderMetricObservationAdmin(ModelView, model=DisorderMetricObservation):
    column_list = [DisorderMetricObservation.id, DisorderMetricObservation.disorder, DisorderMetricObservation.metric_type, "priority", "description"]
    form_columns = [DisorderMetricObservation.disorder, DisorderMetricObservation.metric_type, "priority", "description"]

class MonitoringPlanPatientAdmin(ModelView, model=MonitoringPlanPatient):
    column_list = [MonitoringPlanPatient.id, MonitoringPlanPatient.patient, MonitoringPlanPatient.plan]
    form_columns = [MonitoringPlanPatient.patient, MonitoringPlanPatient.plan]

class MonitoringPlanMetricAdmin(ModelView, model=MonitoringPlanMetric):
    column_list = ["id", MonitoringPlanMetric.plan, MonitoringPlanMetric.metric_type, "frequency", "start_date", "end_date"]
    form_columns = [MonitoringPlanMetric.plan, MonitoringPlanMetric.metric_type, "frequency", "start_date", "end_date"]

def setup_admin(app):
    admin = Admin(app, engine)
    admin.add_view(PatientAdmin)
    admin.add_view(DisorderAdmin)
    admin.add_view(PatientDisorderAdmin)
    admin.add_view(PatientContactRuleAdmin)
    admin.add_view(StorageSettingsAdmin)
    admin.add_view(MetricTypeAdmin)
    admin.add_view(DispensaryObservationAdmin)
    admin.add_view(CDADocumentAdmin)
    admin.add_view(UserAdmin)
    admin.add_view(VoiceInputAdmin)
    admin.add_view(PatientMetricScheduleAdmin)
    admin.add_view(HealthIndicatorAdmin)
    admin.add_view(ReferenceSourceAdmin)
    admin.add_view(MetricReferenceValueAdmin)
    admin.add_view(CDADocumentMetricAdmin)
    admin.add_view(MonitoringPlanAdmin)
    admin.add_view(DisorderMetricObservationAdmin)
    admin.add_view(MonitoringPlanPatientAdmin)
    admin.add_view(MonitoringPlanMetricAdmin)

