#Endpoints: (POST)
#api/pdf-handler/split
#api/pdf-handler/merge
#api/pdf-handler/watermark
#api/pdf-handler/intercalate
#api/pdf-handler/secure/block
#api/pdf-handler/secure/unblock
#api/pdf-handler/enumerate


from django.urls import path

from .views import FileUpload, SplitPDF, BlockPDF, UnblockPDF, IntercalatePDF, MergePDF, WatermarkPDF, EnumeratePDF

urlpatterns = [
    path('upload/', FileUpload.as_view()),
    path('split/', SplitPDF.as_view()),
    path('secure/block/', BlockPDF.as_view()),
    path('secure/unblock/', UnblockPDF.as_view()),
    path('intercalate/', IntercalatePDF.as_view()),
    path('merge/', MergePDF.as_view()),
    path('watermark/', WatermarkPDF.as_view()),
    path('enumerate/', EnumeratePDF.as_view())
]
