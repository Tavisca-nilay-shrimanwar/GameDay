import boto3
from utils import exception_handler, logger
from helper import helper


class GameDay:
    def __init__(self):
        pass

    @exception_handler
    def init(self):
        # health check
        # if health check success
        # call load()
        pass

    @exception_handler
    def load(self):
        # call Blazemeter wait for Peak Load
        # once Peak Load is achieved
        # call chaos()
        pass

    @exception_handler
    def chaos(self):
        # execute custom script
        # wait for script to finish
        # if script finish, call report()
        pass

    @exception_handler
    def report(self):
        # send email
        # capture metrics
        # store in S3
        pass

    def terminate_container(self):
        # terminate container from container
        # invoke lambda(mode="stop", task_name) gracefully shutdown
        # spi
        pass


gameday = GameDay()
gameday.init()
gameday.load()
gameday.chaos()
gameday.report()
gameday.terminate_container()
