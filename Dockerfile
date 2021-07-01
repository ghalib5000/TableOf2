FROM python:3
ADD Table.py /
ENTRYPOINT [ "python", "./Table.py" ]
