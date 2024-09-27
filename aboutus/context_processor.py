from .models import CompanyInfo

def company_info(request):
        profileInfo = CompanyInfo.objects.first()
        return { 'profileInfo' : profileInfo }