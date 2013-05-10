#!/usr/bin/env python
import sys
import os

class command:
    def __init__(self,args):
        self.args = args
    def execute(self):
        try:
            self.__class__.__dict__[self.args[0]](self)
        except KeyError:
            print "There is no command: %s" % ' '.join(self.args)
        except KeyboardInterrupt: pass
    def ls(self):
        objs = []
        options = []
        for item in self.args[1:]:
            if item[0] == '-':
                options.append(item)
            else:
                objs.append(item)

        if not len(objs):
            objs.append(os.getcwd())
            
        files = []
        dirs = []
        for item in objs:
            if os.path.isfile(item):
                files.append(item)
            elif os.path.isdir(item):
                dirs.append(item)

        for item in files:
            print item,

        for item in dirs:
            print '\n\n%s:' % item
            print ' '.join(os.listdir(item))
    def cat(self):
        objs = []
        options = []
        for item in self.args[1:]:
            if item[0] == '-':
                options.append(item)
            else:
                objs.append(item)

        if not len(objs):
            while True:
                strs = raw_input()
                print strs

        for item in objs:
            if os.path.isdir(item):
                print "%s: %s: is a directory" % (self.args[0], item)
            else:
                try:
                    print ''.join(file(item).readlines())
                except:
                    print "%s: %s: does not exist" % (self.args[0], item)
    def echo(self):
        objs = []
        options = []
        for item in self.args[1:]:
            if item[0] == '-':
                options.append(item)
            else:
                objs.append(item)

        for item in objs:
            print r"%s " % item,
    def wc(self):
        objs = []
        options = []
        for item in self.args[1:]:
            if item[0] == '-':
                options.append(item)
            else:
                objs.append(item)

        total_lines = total_words = total_chars = 0
        for item in objs:
            lines = words = chars = 0
            try:
                for line in file(item):
                    chars += len(line)
                    lines += 1
                    words += len(line.split())
                print "%d %d %d %s" % (lines, words, chars, item)
            except:
                print "%s: %s: does not exist" % (self.args[0], item)
            total_lines += lines
            total_words += words
            total_chars += chars
        if len(objs) > 1:
            print "%d %d %d Total" % (total_lines, total_words, total_chars)

        

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "Usage: %s command [options]" % sys.argv[0]
    else:
        c = command(sys.argv[1:])
        c.execute()
