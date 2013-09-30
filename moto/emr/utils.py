import random
import string


def random_job_id(size=13):
    chars = range(10) + list(string.uppercase)
    job_tag = ''.join(unicode(random.choice(chars)) for x in range(size))
    return 'j-{}'.format(job_tag)


def random_instance_group_id(size=13):
    chars = range(10) + list(string.uppercase)
    job_tag = ''.join(unicode(random.choice(chars)) for x in range(size))
    return 'i-{}'.format(job_tag)
