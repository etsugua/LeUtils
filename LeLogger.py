import re

# KNOWN BUGS
## 1 - If msg is too long, without spaces, the findall method skips it

def leLog(msg, format, tag = None, headerChar = None):
    if tag is not None:
        msg = '{:<80}'.format('[' + '{:^7}'.format(tag) + '] : ' + msg + ' ')

    splitMsg = re.findall('.{1,79} |.{1,80}', msg)

    headerLine = None
    if headerChar is not None:
        headerLine = (headerChar * 80)[-80:]

    if headerLine is not None:
        print '\x1b[%sm%s\x1b[0m' % (format, headerLine)

    for split in splitMsg:
        print '\x1b[%sm%s\x1b[0m' % (format, '{:<80}'.format(split))

    if headerLine is not None:
        print '\x1b[%sm%s\x1b[0m' % (format, headerLine)

def leWarn(msg):
    format = ';'.join([str(1), str(7), str(33)])
    leLog(msg, format, 'WARNING', '*')

def leError(msg):
    format = ';'.join([str(1), str(7), str(31)])
    leLog(msg, format, 'ERROR', '*')

def leSuccess(msg):
    format = ';'.join([str(1), str(10), str(32)])
    leLog(msg, format, 'SUCCESS', ' + ')

def leDebug(msg):
    format = ';'.join([str(1), str(10), str(33)])
    leLog(msg, format, 'DEBUG')

def leInfo(msg):
    format = ';'.join([str(1), str(10), str(34)])
    leLog(msg, format, 'INFO')

# TESTS FOR LOGGER
#leWarn('The Quick Brown Fox Jumped Over The Lazy Dog The Quick Brown Fox Jumped Over The Lazy Dog The Quick Brown')
#leError('The Quick Brown Fox Jumped Over The Lazy Dog')
#leSuccess('The Quick Brown Fox Jumped Over The Lazy Dog')
#leDebug('The Quick Brown Fox Jumped Over The Lazy Dog')
#leInfo('TheQuickBrownFoxJumpedOverTheLazyDogTheQuickBrownFoxJumpedOverTheLazyDogTheQuickBrownFoxJumpedOverTheLazyDog')
