from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CalculatorView(APIView):
    def get(self, request, operation):
        instructions = f"Please send a PUT request with the 'a' and 'b' parameters to perform {operation} operation."
        return Response(instructions, status=status.HTTP_200_OK)

    def put(self, request, operation):
        if operation not in ['add', 'sub', 'mul', 'div']:
            return Response("Invalid operation.", status=status.HTTP_400_BAD_REQUEST)

        a = float(request.data.get('a'))
        b = float(request.data.get('b'))

        if operation == 'add':
            result = a + b
        elif operation == 'sub':
            result = a - b
        elif operation == 'mul':
            result = a * b
        elif operation == 'div':
            if b == 0:
                return Response("Division by zero is not allowed.", status=status.HTTP_400_BAD_REQUEST)
            result = a / b

        return Response(f"Result of {operation}: {result}", status=status.HTTP_200_OK)
