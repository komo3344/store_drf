# store_drf
입점사형 스토어 DRF 프로젝트

## 기능
- [x] logging 시스템  
- [ ] 성능모니터링 시스템
  - [ ] prometheus
  - [ ] grabana
- [ ] OAS 3.0 API 문서화  
- [ ] elk system 도입 (elastic search, log stash, kibana)  
- [ ] CI/CD (github action, jenkins)  
- [ ] 무중단배포 (elastic beanstalk 롤링배포 or blue/green 배포)  

## 모델
User (Django의 AbstractBaseUser을 활용하여 email을 기본 id로 사용하도록 구성)
