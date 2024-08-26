```powershell
del .\build\
del .\dist\
del .\dpfm_factory.egg-info\

python setup.py sdist bdist_wheel  
twine upload --repository testpypi dist/*    
```

Then test is out.

Then
```shell
twine upload --repository pypi dist/*    

```
