list=['1.Pythone designed by:\n A.Guido van Rossum B.Dennis Ritchie##A',
      '2.Facebook CEO:\n A.Satya Nadella B.Mark Zuckerberg##B',
      '3.Google New CEO:\n  A.Sundar Pichai B.Larry Page##A',
      '4.Prime minister of India:\n A.Manmohan singh B.Narendra Modi  ##B',
      '5.New Indictrans Technologies Pvt.Ltd.was formed in:\n A.2005 B.2009.##B']
ans_count=0


for element in list:
                                                                          

    """split element of list in 2 parts que & ans"""
    question,answer=element.split('##')                                
    print'\n',question

    """Take i/p from user & check with ans"""
    ans=raw_input('Enter choice :').upper()                         

    
    if ans==answer:                                                 
        ans_count+=1

    else:
        pass

print'\n Your test score is: ', ans_count
