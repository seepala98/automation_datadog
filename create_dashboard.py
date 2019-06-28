import json
import sys
from datadog import initialize, api
from os import path, listdir
from logger import *

#Initializing Logger
logger = log()

class CreateDashboard:
    def __init__(self):
        try:
            logger.info("Loading Datadog options")
            self.options = json.load(open("config/options.json"))
            logger.info("Initializing Datadog api")
            initialize(**self.options)
        except Exception as e:
            logger.error(e)

    def list_dashboard(self):
        logger.info("Listing all datadog dashboard")
        try:
            self.all_dashboard = api.Dashboard.get_all()
            logger.info(self.all_dashboard)
        except Exception as e:
            logger.error(e)

    def create_dashboard(self):
        logger.info("Listing all dashboard template")
        self.dashboard_templates = filter(lambda x:x.endswith(".json"), listdir("config/dashboards"))
        for template in self.dashboard_templates:
            try:
                logger.info("Loading  template: {}".format(template))
                data = json.load(open("config/dashboards/{}".format(template)))
                #print(data)
                if not any(dashboard for dashboard in self.all_dashboard['dashboards'] if dashboard['title'] == data['title']):
                    logger.info("Creating Dashboard: {}".format(data.get("title")))
                    logger.info(api.Dashboard.create(**data))
                else:
                    logger.info("Dashboard: {} already exists".format(data.get("title")))
            except Exception as e:
                logger.error(e)

d = CreateDashboard()
d.list_dashboard()
d.create_dashboard()
