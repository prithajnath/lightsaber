FROM public.ecr.aws/lambda/python:3.9

RUN pip install python-youtube --target "${LAMBDA_TASK_ROOT}"

COPY app.py ${LAMBDA_TASK_ROOT}

CMD ["app.handler"]

