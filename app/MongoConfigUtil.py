#!/usr/bin/env python
# encoding: utf-8

'''
File: MongoConfigUtil.py
Author: NYU ITP Team
Description: Configuration helper tool for MongoDB related Map/Reduce jobs Instance based, more idiomatic for those who prefer it to the static methoding of ConfigUtil
'''
import logging
import bson

default_config = {
        "jobVerbose" : False,
        "jobBackground" : False,
        "jobMapper" : "",
        "jobReducer" : "",
        "jobCombiner" : "",
        "jobPartitioner" : "",
        "jobSortComparator" : "",
        "jobMapperOutputKey" : "",
        "jobMapperOutputValue" : "",
        "jobInputFormat" : "",
        "jobOutputFormat" : "",
        "jobOutputKey" : "",
        "jobOutputValue" : "",
        "inputURI" : "",
        "outputURI" : "",
#        "INPUT_SPLIT_SIZE" : Value to specify how many docs input is split into. Affects the number of mappers.,
        "splitSize" : 8,
        "splitKey" : {'_id' : 1},
        "createInputSplits" : True,
        "splitsUseShards" : False,
        "splitsUseChunks" : True,
        "splitsSlaveOK" : False,
        "limit" : 0,
        "skip" : 0,
        "inputKey" : "",
        "sort" : "",
        "is_no_timeout" : False,
        "fields" : "",
        "query" : "",
        "collection_name" : "in",
        "db_name" : "test",
        }
