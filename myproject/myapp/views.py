from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentDetail(APIView):
    
    def get(self, request):
        '''
        If user enter stu_id then it return data for that student else return all data.
        '''        
        try:
            payload = request.data
            id = payload.get('stu_id')
            
            if id:
                stu_obj = Student.objects.filter(stu_id = id).first()
                if not stu_obj:
                    result = [{
                        'Status' : False,
                        'Error'  : f'Data with student id = {id} is not present in database.',
                        'Data'   : None
                    }]
                    return Response(result)
                
                serializer = StudentSerializer(stu_obj)
                result = [{
                    'Status'    : True,
                    'Msg'       : 'Data Found',
                    'Data'      : serializer.data
                }]
                return Response(result)
                
            stu_obj = Student.objects.all().values(
                'stu_id', 'name', 'roll_no', 'class_no', 'section', 'created_on', 'updated_on'
                )
            stu_data = list(stu_obj)
            
            if not stu_obj:
                return Response({
                    'Status'    : True,
                    'Msg'       : 'Data Not present in Database',
                    'Data'      : None
                })
                
            serializer = StudentSerializer(stu_data, many = True)
            result = [{
                'Status' : True,
                'Msg'    : 'Data Found',
                'Data'   : serializer.data
            }]
            return Response(result)
        
        except Exception as e:
            result = [{
                'Status' : False,
                'Error'  : str(e)                
            }]
            return Response(result)
        
    def post(self, request):
        '''
        Create New Entry in Database.
        '''
        payload = request.data               
        serializer = StudentSerializer(data = payload)
        if serializer.is_valid():
            serializer.save()
            result = [{
                'Status' : True,
                'Msg'    : 'Data added successfullly',
                'Data'   : serializer.data
            }]
            return Response(result)
        
        result = [{
            'Status' : False,
            'Error'  : 'Data is not Valid',
            'Data'   : serializer.errors
        }]
        return Response(result)
         
    def patch(self, request):
        '''
        Update the existing data in Database.
        '''
        payload = request.data
        id = payload.get('stu_id')
        
        if not id :
            result = [{
                'Status' : False,
                'Error'  : 'Student id is required',
                'Data'   : None
            }]
            return Response(result)
        
        try:
            stu_obj = Student.objects.get(stu_id = id)
            
        except Student.DoesNotExist:
            result= [{
                'Status'   : False,
                'Error'    : f'Data with student id = {id} is not present in database.',
                'Data'     : None
            }]
            return Response(result)
            
        serializer = StudentSerializer(stu_obj, data= payload, partial= True)
        if serializer.is_valid():
            serializer.save()
            result = [{
                'Status' : True,
                'Msg'    : 'Data Updated Successfully',
                'Data'   : serializer.data
            }]
            return Response(result)
        
        result = [{
            'Status'  : False,
            'Error'   : serializer.errors,
            'Data'    : None
        }]
        return Response(result)
    
    def delete(self, request):
        '''
        Delete data from Database.
        '''
        payload = request.data
        id = payload.get('stu_id')
        if not id :
            result = [{
                'Status' : False,
                'Error'  : 'Student id is required',
                'Data'   : None
            }]
            return Response(result)
        
        stu_obj = Student.objects.filter(stu_id = id)
            
        if not stu_obj:
            result = [{
                'Status' : False,
                'Error'  : f'Data with student id = {id} is not present in database.',
                'Data'   : None
            }]
            return Response(result)
            
        stu_obj.delete()
        result =[{
            'Status' : True,
            'Msg'    : 'Data deleted successfully.'
        }]

        return Response(result)
        
                


