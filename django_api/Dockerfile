FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install pip and pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock first (for caching)
COPY Pipfile Pipfile.lock ./

# Install dependencies via pipenv
RUN pipenv install --skip-lock --dev

# Copy the rest of the project
COPY . .

ENTRYPOINT ["pipenv", "run"]
